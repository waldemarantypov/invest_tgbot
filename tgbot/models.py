import requests

from django.db import models, IntegrityError, DataError
from tgbot import utils

import yfinance as yf


class User(models.Model):
    """All data for each user"""

    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32, null=True, blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, null=True, blank=True)
    language_code = models.CharField(max_length=8, null=True, blank=True, help_text="Telegram client's lang")
    deep_link = models.CharField(max_length=64, null=True, blank=True)

    user_currency = models.CharField(max_length=6, null=True, blank=True)
    user_trade_experience = models.CharField(max_length=3, null=True, blank=True)

    interested_in_bot_mark = models.CharField(max_length=30, null=True, blank=True)

    is_blocked_bot = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    @classmethod
    def get_user_and_created(cls, update, context):
        """ python-telegram-bot's Update, Context --> User instance """
        data = utils.extract_user_data_from_update(update)
        u, created = cls.objects.update_or_create(user_id=data["user_id"], defaults=data)

        if created:
            if context is not None and context.args is not None and len(context.args) > 0:
                payload = context.args[0]
                if str(payload).strip() != str(data["user_id"]).strip():  # you can't invite yourself
                    u.deep_link = payload
                    u.save()

        return u, created

    @classmethod
    def get_user_and_updated_currency(cls, update, context, currency):
        u = cls.get_user(update, context)
        u.user_currency = currency
        u.save()

    @classmethod
    def get_user_and_updated_trade_experience(cls, update, context, trade_experience):
        u = cls.get_user(update, context)
        u.user_trade_experience = trade_experience
        u.save()

    @classmethod
    def get_user_and_updated_language_code(cls, update, context, language_code):
        u = cls.get_user(update, context)
        u.language_code = language_code
        u.save()

    @classmethod
    def get_user(cls, update, context):
        u, _ = cls.get_user_and_created(update, context)
        return u

    @classmethod
    def get_user_and_updated_interested_mark(cls, update, context, mark):
        u = cls.get_user(update, context)
        u.interested_in_bot_mark = mark
        u.save()

    @classmethod
    def get_user_by_username_or_user_id(cls, string):
        """ Search user in DB, return User or None if not found """
        username = str(string).replace("@", "").strip().lower()
        if username.isdigit():  # user_id
            return cls.objects.filter(user_id=int(username)).first()
        return cls.objects.filter(username__iexact=username).first()

    def invited_users(self):  # --> User queryset 
        return User.objects.filter(deep_link=str(self.user_id), created_at__gt=self.created_at)


class Portfolio(models.Model):
    """Portfolio to exact User"""

    to_invest = models.FloatField(default=0.0)
    pf_price = models.FloatField(default=0.0)
    pf_costs = models.FloatField(default=0.0)
    pf_earn = models.FloatField(default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Portfolio of User with username: @{self.user.username} and Total Portfolio Price is: {self.pf_price}"

    @staticmethod
    def get_or_create_by_user(user):
        portfolio = Portfolio.objects.get_or_create(user=user)
        return portfolio[0]

    def update_to_invest(self, to_invest):
        self.to_invest = round(to_invest, 2)
        self.save()

    def update_pf_without_regular_prices(self):
        stocks = Stock.filter_by_portfolio(self)
        total_pf_price = 0
        total_pf_costs = 0
        for stock in stocks:
            #stock.update_prices_yf()
            total_pf_costs += stock.total_costs
            total_pf_price += stock.total_price
        total_pf_earn = total_pf_price - total_pf_costs
        self.pf_price = round(total_pf_price, 2)
        self.pf_costs = round(total_pf_costs, 2)
        self.pf_earn = round(total_pf_earn, 2)
        self.save()

    def update_pf_with_regular_prices(self):
        stocks = Stock.filter_by_portfolio(self)
        total_pf_price = 0
        total_pf_costs = 0
        for stock in stocks:
            stock.update_prices_yf()
            total_pf_costs += stock.total_costs
            total_pf_price += stock.total_price
        total_pf_earn = total_pf_price - total_pf_costs
        self.pf_price = round(total_pf_price, 2)
        self.pf_costs = round(total_pf_costs, 2)
        self.pf_earn = round(total_pf_earn, 2)
        self.save()

class Stock(models.Model):
    """Every Stocks connected to Portfolio"""

    symbol = models.CharField(max_length=16)
    shares = models.FloatField(default=0.0)
    regular_price = models.FloatField(default=0.0)
    total_price = models.FloatField(default=0.0)
    total_costs = models.FloatField(default=0.0)
    earned_money = models.FloatField(default=0.0)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.symbol} in Portfolio ID: {self.portfolio.id}"

    @staticmethod
    def create_by_portfolio(portfolio, symbol):
        stock = Stock.objects.create(portfolio=portfolio, symbol=symbol)
        stock.save()
        pass

    @staticmethod
    def filter_by_portfolio(portfolio):
        stocks = Stock.objects.filter(portfolio=portfolio)
        return stocks

    def update_prices_yf(self, currency_rates):
        ticker = yf.Ticker(self.symbol).info
        currency_rate = currency_rates[ticker['currency']] if ticker['currency'] != 'USD' else 1
        self.regular_price = round((ticker['regularMarketPrice']/currency_rate), 2)
        self.total_price = round(self.regular_price * self.shares, 2)
        self.save()

    def update_earned_money(self):
        self.earned_money = round(self.total_price - self.total_costs, 2)
        self.save()

    @staticmethod
    def list_of_stock_symbols_in_portfolio(portfolio):
        stocks = Stock.filter_by_portfolio(portfolio)
        list_of_stock_symbols =[]
        for stock in stocks:
            list_of_stock_symbols.append(stock.symbol)
        return list_of_stock_symbols

    @staticmethod
    def get_stock_by_symbol(portfolio, symbol):
        stock = Stock.objects.get(portfolio=portfolio, symbol=symbol)
        return stock

    @staticmethod
    def update_shares_of_stock(stock, shares):
        stock.shares = shares
        stock.save()

    @staticmethod
    def update_total_costs_of_stock(stock, total_costs):
        stock.total_costs = round(total_costs, 2)
        stock.save()


class Transaction(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    stock_price = models.FloatField(default=0.0)
    stock_amount = models.FloatField(default=0.0)
    total_transaction_sum = models.FloatField(default=0.0)

    def __str__(self):
        stock = f"{self.stock.symbol}" if self.stock != 0 else 'NO stocks'
        return f"Transaction for Stock {stock} with Total Transaction Sum: {self.total_transaction_sum}"


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user: {self.user}, created at {self.created_at.strftime('(%H:%M, %d %B %Y)')}"

    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)
        # Parse location with arcgis
        from .tasks import save_data_from_arcgis
        save_data_from_arcgis.delay(latitude=self.latitude, longitude=self.longitude, location_id=self.pk)


class Arcgis(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE, primary_key=True)

    match_addr = models.CharField(max_length=200)
    long_label = models.CharField(max_length=200)
    short_label = models.CharField(max_length=128)

    addr_type = models.CharField(max_length=128)
    location_type = models.CharField(max_length=64)
    place_name = models.CharField(max_length=128)

    add_num = models.CharField(max_length=50)
    address = models.CharField(max_length=128)
    block = models.CharField(max_length=128)
    sector = models.CharField(max_length=128)
    neighborhood = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    metro_area = models.CharField(max_length=64)
    subregion = models.CharField(max_length=64)
    region = models.CharField(max_length=128)
    territory = models.CharField(max_length=128)
    postal = models.CharField(max_length=128)
    postal_ext = models.CharField(max_length=128)

    country_code = models.CharField(max_length=32)

    lng = models.DecimalField(max_digits=21, decimal_places=18)
    lat = models.DecimalField(max_digits=21, decimal_places=18)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location}, city: {self.city}, country_code: {self.country_code}"

    @classmethod
    def from_json(cls, j, location_id):
        a = j.get("address")
        l = j.get("location")

        if "address" not in j or "location" not in j:
            return

        arcgis_data = {
            "match_addr": a.get("Match_addr"),
            "long_label": a.get("LongLabel"),
            "short_label": a.get("ShortLabel"),
            "addr_type": a.get("Addr_type"),
            "location_type": a.get("Type"),
            "place_name": a.get("PlaceName"),
            "add_num": a.get("AddNum"),
            "address": a.get("Address"),
            "block": a.get("Block"),
            "sector": a.get("Sector"),
            "neighborhood": a.get("Neighborhood"),
            "district": a.get("District"),
            "city": a.get("City"),
            "metro_area": a.get("MetroArea"),
            "subregion": a.get("Subregion"),
            "region": a.get("Region"),
            "territory": a.get("Territory"),
            "postal": a.get("Postal"),
            "postal_ext": a.get("PostalExt"),
            "country_code": a.get("CountryCode"),
            "lng": l.get("x"),
            "lat": l.get("y")
        }

        arc, _ = cls.objects.update_or_create(location_id=location_id, defaults=arcgis_data)
        return

    @staticmethod
    def reverse_geocode(lat, lng):
        r = requests.post(
            "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode",
            params={
                'f': 'json',
                'location': f'{lng}, {lat}',
                'distance': 50000,
                'outSR': '',
            },
            headers={
                'Content-Type': 'application/json',
            }
        )
        return r.json()


class UserActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"user: {self.user}, made: {self.action}, created at {self.created_at.strftime('(%H:%M, %d %B %Y)')}"