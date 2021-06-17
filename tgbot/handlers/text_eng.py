# command start
start_created = "Hello, {first_name}!\n\n"
start_created_portfolio = 'To Configure your portfolio - /portfolio\n\n'
start_created_feedback = 'If you will have a minute to answer 5 questions - press /feedback\n' \
                         'Your answers will help us to make the bot more useful.\n\n'
start_created_portfolio_example = "This is how the portfolio will look like:"
start_created_share = 'You can simply share the bot by sending this message: {share_url}'
start_created_share_command = 'You can get your unique link to share it with your friends here:' \
                              ' /share'
start_change_language = 'To Сhange bot language: /language'
start_created_inbaze = 'Ещё у нас есть телеграм канал, где рассказываем про финансовую грамотность: @inbaze'

# OKAY
# command feedback
feedback = "Fill out the Google Form survey, so I can understand how useful I am: {google_form_link}"
# OKAY

# command share
share_command = "You can share the bot by sending the message below:\n\n"
share_message = "Hi!\n\n" \
                "My name is Inbaze and I am a portfolio-bot 🤖\n" \
                "I help to track the UPs 📈 / DOWNs 📉 of your investment portfolio (stocks and cryptocurrencies).\n\n" \
                "The bot is completely free. Welcome!\n" \
                "{share_url}"

# command portfolio
wait_for_portfolio = 'Have a patience - this may take a while ⏱\n\n' # \
                     # 'The larger the portfolio - the more information to collect on it 🤓\n'
# OKAY
portfolio_head = 'Portfolio:\n'
to_invest_text = 'To invest'
total_portfolio = 'Current value'
net_profit_button = 'Net'
total_profit_button = 'Total'
costs_button = 'Costs'
efficiency_button = '%'
amount_button = 'Amount'
update_button = '💸 Update portfolio'

wait_update = 'The portfolio is being updated - it may take a couple of minutes ⏱'

modify_button = '💼 Modify»'
modify_question = 'What do you want to do?'

balance_button = '✏️ Modify balances»'
add_stock_button = '➕ Add new asset»'
delete_stock_button = '➖ Delete asset»'
close_button = '❌ Close'
close_modify_menu_portfolio = 'Good.\n\n' \
                              'If you want to take another look at the portfolio - press /portfolio.\n' \
                              'If you want to leave feedback - press /feedback\n' \
                              'If you want to share the bot with your friends - press /share'
# OKAY

change_balance_text = 'Enter the symbol of the stock / cryptocoin that you want to CHANGE ✏️\n\n' \
                      '<i>(Tesla has a symbol - TSLA, and bitcoin - "BTC-USD")</i>.'
add_stock_text = 'Enter the symbol of the stock / cryptocoin that you want to ADD ➕\n\n' \
                 '<i>(Tesla has a symbol - TSLA, and bitcoin - "BTC-USD")</i>.\n\n' \
                 'p.s. If you are not sure about the asset\'s ticker' \
                 ' - you can check it here: https://finance.yahoo.com'
delete_stock_text = 'Enter the symbol of the stock / cryptocoin that you want to DELETE ❌\n\n' \
                    '<i>(Tesla has a symbol - TSLA, and bitcoin - "BTC-USD")</i>.' \
    # okay

modify_to_invest_button = 'Edit money to invest'
back_to_modify_button = '🔙 Back'
# okay
change_balance_text_stock_write = 'In the process ⏱'
delete_stock_write = 'In the process ⏱'
add_stock_write = 'In the process ⏱'
# okay

wrong_ticket = 'Try to enter a ticker again\n\n<i>You can use: a-z, A-Z, 0-9, "." and "-".</i>\n' \
                      '<i>Number of symbols: 2-16.\n\n' \
                      '(Example:  <b>SBER.ME</b>, <b>BTC-USD</b>)</i>'
modify_wrong_stock_parameters = 'Try to enter these parameters again\n\n' \
                                '<i>You can use: 0-9 and "."\n\n' \
                                '(Example: 2 - "2", 2,53 - "2.53")</i>'

wrong_text_entered = "Sorry, I didn\'t understand: '{text}'"

# okay

modify_balance_stock_not_in_portfolio = 'Error: this position is not included into portfolio, or this ticker does not exist.\n\n' \
                                        '<i>In the first case you should add a ticker via "➕ Add new asset</i>"\n' \
                                        '<i>In the second case you should try to find ticker here https://finance.yahoo.com</i>'
modify_balance_stock_symbol_shares = 'Currently you have <b><i>{shares}</i></b> shares of <b><i>{symbol}</i></b>\n' \
                                     'What would be the new balance of {symbol}?\n\n' \
                                     '<i>(For example: 2  - "2",2,53 - "2.53")</i> \n\n'
delete_stock_info = 'Currently you have <b><i>{shares}</i></b> shares / crypto coins of <b><i>{symbol}</i></b>.\n' \
                    'Do you want to remove this asset from your portfolio?'
delete_stock_success = 'You have removed <b><i>{symbol}</i></b> from the portfolio, I hope you closed it profitably 🙏'
delete_stock_cancel = "We won't remove <b><i>{symbol}</i></b>, okay"
delete_stock_yes_text = 'Delete 🗑'
delete_stock_no_text = 'Save ❤️'
# okay
modify_balance_stock_shares_success = '👍 Updated!\n\nNow you have <b><i>{shares}</i></b> shares / crypto coins of <b><i>{stock}</i></b>\n' \
                                      'Enter the amount that you spent to purchase these number of shares / crypto coins?\n\n' \
                                      '<i>Example: 100 dollars and 27 cents - 100.27</i>'
modify_balance_stock_total_costs_success = '✅ Updated!\n\n' \
                                           'To sum it up:\n' \
                                           'You spent <b><i>{total_costs}</i></b> buying <b><i>{shares}</i></b>' \
                                           ' shares / cryptocoins of <b><i>{stock}</i></b>'
# okay
change_to_invest_text = 'Your current balance is: <b><i>{to_invest}</i></b>\n\n' \
                        'How much do you want to add for the balance?'
changed_to_invest_text = 'Great! I have updated your balance and now it is: <b><i>{to_invest}</i></b>\n'

add_stock_symbol_check_already_have = 'You already have <b><i>{shares}</i></b> shares / crypto coins of <b><i>({symbol})</i></b>.\n\n' \
                                      'If you want to change the balance of the stock - choose "✏️ Edit asset"' \
                                      ' in /portfolio).'
add_stock_symbol_check_success = '👍 <b><i>{symbol}</i></b> was added into portfolio.\n\n' \
                                 'How much <b><i>{symbol}</i></b> do you want to add?\n\n' \
                                 '<i>(Example: 2 - "2", 2,53 - "2.53")</i>\n\n'
add_stock_not_in_yfinance = 'Error: You entered the stock / crypto coin symbol incorrectly.\n\n' \
                            '<i>See the correct spelling of the symbol here https://finance.yahoo.com</i>'

language_ask = 'Choose language:'
language_EN = "🇺🇸"
language_RU = "🇷🇺"
language_modefied_succes = "Language changed successfully!"
# okay
# дальше не трогаем

broadcast_command = '/broadcast'

broadcast_no_access = "Sorry, you don't have access to this function."
broadcast_header = "This message will be sent to all users.\n\n"
confirm_broadcast = "Confirm ✅"
decline_broadcast = "Decline ❌"
message_is_sent = "Message is sent ✅\n\n"
declined_message_broadcasting = "Message broadcasting is declined ❌\n\n"

error_with_markdown = "Can't parse your text in Markdown style."
specify_word_with_error = " You have mistake in the word "

secret_admin_commands = "⚠️ Secret Admin commands\n" \
                        "/stats - bot stats"

not_admin_answer = "You are not a admin!"

unlock_secret_room = "Congratulations! You've opened a secret room👁 ‍🗨. There is some information for you:\n" \
                     "*Users*: {user_count}\n" \
                     "*24h active*: {active_24}"

share_location = "Would you mind sharing your location?"
thanks_for_location = "Thanks for 🌏🌎🌍"
