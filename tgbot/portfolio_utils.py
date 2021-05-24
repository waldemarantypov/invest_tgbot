import time
from datetime import date

# Raw Package
import numpy as np
import pandas as pd

# Data Source
import yfinance as yf

from tgbot.handlers.static_text import to_invest_text, total_portfolio

# Data Viz
import plotly.graph_objs as go

# print(yf.download(tickers='UBER', period='5d', interval='5m'))

# msft = yf.Ticker("msft")
# print(msft.info['regularMarketPrice'])

import requests

currency_dict = {}
date_today = ''


def currency_exchange():
    global currency_dict
    global date_today
    check_date_today = date.today()
    check_date_today = check_date_today.strftime("%d/%m/%Y")
    if date_today != check_date_today:
        cur_api_url = 'https://openexchangerates.org/api/latest.json'

        params = {
            'app_id': 'd21a0e41164d42b0b4b59ddc59325c9b',
        }
        res = requests.get(cur_api_url, params=params)
        currency_dict = res.json()['rates']
        date_today = check_date_today
    return currency_dict


def portfolio_update(portfolio, stocks):
    currency_rates = currency_exchange()
    for stock in stocks:
        stock.update_prices_yf(currency_rates)
        stock.update_earned_money()
    portfolio.update_pf_without_regular_prices()
    pass


def string_format(f, s, total_add=0, symbol='$', format='n'):
    l = 30
    c1 = ': '
    c2 = '> '
    bet = '–' * (l + total_add - len(f + c1 + c2 + s + symbol))
    if format == 'n':
        string = '{f}{c1}{bet}{c2}{s}{symbol}\n'.format(f=f, c1=c1, bet=bet, c2=c2, s=s, symbol=symbol)
    elif format == 'b':
        string = '<b>{f}</b>{c1}{bet}{c2}<b>{s}{symbol}</b>\n'.format(f=f, c1=c1, bet=bet, c2=c2, s=s, symbol=symbol)
    return string


def output_style(output):
    start = '<pre>'
    end = '</pre>'
    return start + output + end


def portfolio_output_net(portfolio, stocks):
    f = to_invest_text
    s = str(portfolio.to_invest)

    c3 = ('–' * 30) + '\n'

    output_text = string_format(f, s)

    output_text += c3

    f = 'Stock'
    '''
    Change 's' for every function 
    '''
    s = 'Net'
    output_text += string_format(f, s, symbol='', format='b')

    for stock in stocks:
        f = stock.symbol
        '''
        Change 's' for every function 
        '''
        s = str(stock.earned_money)
        output_text += string_format(f, s)

    output_text += c3

    f = total_portfolio
    '''
    Change 's' for every function 
    '''
    s = str(portfolio.pf_earn)
    output_text += string_format(f, s, format='b')

    output_text = output_style(output_text)

    return output_text


def portfolio_output_total(portfolio, stocks):
    f = to_invest_text
    s = str(portfolio.to_invest)

    c3 = ('–' * 30) + '\n'

    output_text = string_format(f, s)

    output_text += c3

    f = 'Stock'
    '''
    Change 's' for every function 
    '''
    s = 'Total'
    output_text += string_format(f, s, symbol='', format='b')

    for stock in stocks:
        f = stock.symbol
        '''
        Change 's' for every function 
        '''
        s = str(stock.total_price)
        output_text += string_format(f, s)

    output_text += c3

    f = total_portfolio
    '''
    Change 's' for every function 
    '''
    s = str(portfolio.pf_price)
    output_text += string_format(f, s, format='b')

    output_text = output_style(output_text)

    return output_text


def portfolio_output_costs(portfolio, stocks):
    f = to_invest_text
    s = str(portfolio.to_invest)

    c3 = ('–' * 30) + '\n'

    output_text = string_format(f, s)

    output_text += c3

    f = 'Stock'
    '''
    Change 's' for every function 
    '''
    s = 'Costs'
    output_text += string_format(f, s, symbol='', format='b')

    for stock in stocks:
        f = stock.symbol
        '''
        Change 's' for every function 
        '''
        s = str(stock.total_costs)
        output_text += string_format(f, s)

    output_text += c3

    f = total_portfolio
    '''
    Change 's' for every function 
    '''
    s = str(portfolio.pf_costs)
    output_text += string_format(f, s, format='b')

    output_text = output_style(output_text)

    return output_text


def portfolio_output_amount(portfolio, stocks):
    f = to_invest_text
    s = str(portfolio.to_invest)

    c3 = ('–' * 30) + '\n'

    output_text = string_format(f, s)

    output_text += c3

    f = 'Stock'
    '''
    Change 's' for every function 
    '''
    s = 'Amount'
    output_text += string_format(f, s, symbol='', format='b')

    for stock in stocks:
        f = stock.symbol
        '''
        Change 's' for every function 
        '''
        s = str(stock.shares)
        output_text += string_format(f, s, symbol='')

    output_text += c3

    f = total_portfolio
    '''
    Change 's' for every function 
    '''
    s = str(portfolio.pf_price)
    output_text += string_format(f, s, format='b')

    output_text = output_style(output_text)

    return output_text


def portfolio_output_efficiency(portfolio, stocks):
    f = to_invest_text
    s = str(portfolio.to_invest)

    c3 = ('–' * 30) + '\n'

    output_text = string_format(f, s)

    output_text += c3

    f = 'Stock'
    '''
    Change 's' for every function 
    '''
    s = 'Efficiency'
    output_text += string_format(f, s, symbol='', format='b')

    for stock in stocks:
        f = stock.symbol
        '''
        Change 's' for every function 
        '''
        s_efficiency = round((stock.earned_money / stock.total_costs) * 100, 2) if stock.total_costs != 0 else 0.00
        s = str(s_efficiency)
        output_text += string_format(f, s, symbol='%')

    output_text += c3

    f = total_portfolio
    '''
    Change 's' for every function 
    '''
    pf_efficiency = round((portfolio.pf_earn / portfolio.pf_costs) * 100, 2) if portfolio.pf_costs != 0 else 0.00
    s = str(pf_efficiency)
    output_text += string_format(f, s, symbol='%', format='b')

    output_text = output_style(output_text)

    return output_text


def portfolio_summary(portfolio, stocks):
    output_text = f'{to_invest_text} - {portfolio.to_invest}\n'
    output_text += f'Сток - Шэры - Косты - Прайс - НэтПрофит - Эф, %\n'

    for stock in stocks:
        stock.update_prices_yf()
        stock.update_earned_money()

        s_efficiency = (stock.earned_money / stock.total_costs) * 100 if stock.total_costs != 0 else 0

        if s_efficiency < 0:
            s_efficiency = f'-{round(s_efficiency, 2)}'
        elif s_efficiency > 0:
            s_efficiency = f'+{round(s_efficiency, 2)}'
        else:
            s_efficiency = '0.0'
        output_text += '* {symbol} - {amount} - {total_costs} - {total_price} - {earned_money} - {s_efficiency}\n' \
            .format(symbol=stock.symbol, amount=stock.shares, total_costs=stock.total_costs,
                    total_price=stock.total_price, earned_money=stock.earned_money, s_efficiency=s_efficiency)
    portfolio.update_pf_without_regular_prices()
    pf_efficiency = (portfolio.pf_earn / portfolio.pf_costs) * 100 if portfolio.pf_costs != 0 else 0
    if pf_efficiency < 0:
        pf_efficiency = f'-{round(pf_efficiency, 2)}%'
    elif pf_efficiency > 0:
        pf_efficiency = f'+{round(pf_efficiency, 2)}%'
    else:
        pf_efficiency = '0.0'
    output_text += f'{total_portfolio} - {portfolio.pf_costs} - {portfolio.pf_price} - {portfolio.pf_earn} - {pf_efficiency}'
    return output_text
