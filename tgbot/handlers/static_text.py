# command start
start_created = "Привет, {first_name}!\n\n"
start_created_portfolio = 'Если хочешь перейти к портфелю - жми или пиши: /portfolio\n\n'
start_created_feedback = 'Если будет минута чтобы ответить на 5 вопросов - жми сюда /feedback\n\n' \
                         'Это поможет мне сделать бот полезней.\n\n' \
                         'Ещё у нас есть телеграм канал, где рассказываем про финансовую грамотность: @inbaze'
start_created_portfolio_example = "Вот так будет выглядеть портфель:"

# OKAY
# command feedback
feedback = "Я хочу понять насколько мой функционал полезен. 🙏\n\n" \
           "Заполни гугл-форму, пожалуйста: {google_form_link}"
# OKAY
# command portfolio
wait_for_portfolio = 'Терпение - это может занять несколько минут. \n\n' \
                     'Чем больше портфель - тем больше собирать по нему информацию 🤓\n'
# OKAY
portfolio_head = 'Portfolio:\n'
to_invest_text = 'Готов инвестировать'
total_portfolio = 'Текущая стоимость'
net_profit_button = 'Чистый доход'
total_profit_button = 'Итог'
costs_button = 'Затраты'
efficiency_button = '%'
amount_button = 'Кол-во'
update_button = '💸 Обновить портфель'

wait_update = 'Портфолио обновляется ⏱ - может занять пару минут.'

modify_button = '💼 Поменять»'
modify_question = 'Что менять?'

balance_button = '✏️ Изменить актив'
add_stock_button = '➕ Добавить актив'
delete_stock_button = '➖ Удалить актив'
close_button = '❌ Ничего'
close_modify_menu_portfolio = 'Хорошо.\n\n' \
                              'Если захочешь взглянуть на портфель еще раз: /portfolio.\n' \
                              'Если хочешь оставить фидбек: /feedback'
# OKAY

change_balance_text = 'Введи cимвол акции / криптомонеты, которую хочешь ИЗМЕНИТЬ ✏️\n\n' \
                      '<i>(У Tesla символ - TSLA, а у биткоина к доллару - "BTC-USD")</i>.'
add_stock_text = 'Введи cимвол акции / криптомонеты, которую хочешь ДОБАВИТЬ ➕\n\n' \
                 '<i>(У Tesla символ - TSLA, а у биткоина к доллару - "BTC-USD")</i>.'
delete_stock_text = 'Введи cимвол акции / криптомонеты, которую хочешь УДАЛИТЬ ❌\n\n' \
                    '<i>(У Tesla символ - TSLA, а у биткоина к доллару - "BTC-USD")</i>.' \
    # okay

modify_to_invest_button = 'Поменять баланс будущих инвестиций'
back_to_modify_button = '🔙 Назад'
# okay
change_balance_text_stock_write = 'В процессе ⏱'
delete_stock_write = 'В процессе ⏱'
add_stock_write = 'В процессе ⏱'
# okay
modify_wrong_ticket = 'Попробуй ввести еще раз)\n\n<i>Используй: a-z, A-Z, 0-9, . и -.</i>\n' \
                      '<i>Кол-во символов: 3-6.\n\n' \
                      '(Пример:  <b>SBER.ME</b>, <b>BTC-USD</b>)</i>'
modify_wrong_stock_parameters = 'Попробуй ввести еще раз)\n\n' \
                                '<i>Используй: 0-9 и "."\n\n' \
                                '(Пример: 2 - "2", 2,53 - "2.53")</i>'
add_wrong_ticket = 'Попробуй ввести еще раз)\n<i>Используй: a-z, A-Z, 0-9, . и -.</i>\n' \
                   '<i>Кол-во символов: 3-6.</i>'
delete_wrong_ticket = 'Попробуй ввести еще раз)\n<i>Используй: a-z, A-Z, 0-9, . и -.</i>\n' \
                      '<i>Кол-во символов: 3-6.</i>'
# okay
modify_balance_stock_not_in_portfolio = 'Ошибка: этой позиции нет в портфеле, либо ее в принципе не существует.\n\n' \
                                        '<i>Если первый вариант - добавь тикер через "➕ Добавить актив</i>"\n' \
                                        '<i>Если второй вариант - посмотри название тикера тут https://finance.yahoo.com</i>'
modify_balance_stock_symbol_shares = 'В портфеле сейчас {shares} акций {symbol}.\n' \
                                     'На сколько изменяем?\n\n' \
                                     '<i>(Пример: 2 акции - "2",2,53 - "2.53")</i> \n\n'
delete_stock_info = 'В портфеле сейчас <b><i>{shares}</i></b> акций / криптомонет <b><i>{symbol}</i></b>.\n' \
                    'Хочешь удалить эту акцию / криптомонету из своего портфеля?'
delete_stock_success = 'Ты удалил <b><i>{symbol}</i></b> с портфеля, надеюсь выгодно ушла 🙏'
delete_stock_cancel = 'Не продаем <b><i>{symbol}</i></b>, хорошо'
delete_stock_yes_text = 'Удалить 🗑'
delete_stock_no_text = 'Оставить ❤️'
# okay
modify_balance_stock_shares_success = '👍 Обновил!\n\nТеперь у тебя <b><i>{shares}</i></b> акций <b><i>{stock}</i></b>\n' \
                                      'Введи, какая сумма потрачена на покупку этого кол-во акций / криптомонет?\n\n' \
                                      '<i>Пример: 100 долларов и 27 центов - 100.27</i>'
modify_balance_stock_total_costs_success = '✅ Обновил!\n\n' \
                                           'Итог: потрачено <b><i>{total_costs}</i></b> на покупку <b><i>{shares}</i></b>' \
                                           ' акций / криптомонет <b><i>{' \
                                           'stock}</i></b>\n '
# okay
change_to_invest_text = 'У тебя сейчас: <b><i>{to_invest}</i></b>\n\n' \
                        'Какой будет новая сумма?'
changed_to_invest_text = 'Cупер! Я обновил твой баланс, и теперь он равен: <b><i>{to_invest}</i></b>\n'

add_stock_symbol_check_already_have = 'У тебя уже есть позиция <b><i>({symbol})</i></b> в размере <b><i>{shares}</i></b>.\n\n' \
                                      'Если хочешь изменить баланс актива - выбери "✏️ Изменить актив"' \
                                      'в /portfolio).'
add_stock_symbol_check_success = '👍 <b><i>{symbol}</i></b> добавлен в портфель.\n\n' \
                                 'Сколько акций / криптомонет хочешь добавить?\n\n' \
                                 '<i>(Пример 2 акции - "2", 2,53 - "2.53")</i>\n\n'
add_stock_not_in_yfinance = 'Ошибка: ты не правильно ввел символ акции / криптомонеты\n\n' \
                            '<i>Посмотри правильно написание символа тут https://finance.yahoo.com</i>'
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
specify_word_with_error = " You have mistake with the word "

secret_admin_commands = "⚠️ Secret Admin commands\n" \
                        "/stats - bot stats"

not_admin_answer = "You are not a admin!"

unlock_secret_room = "Congratulations! You've opened a secret room👁 ‍🗨. There is some information for you:\n" \
                     "*Users*: {user_count}\n" \
                     "*24h active*: {active_24}"

share_location = "Would you mind sharing your location?"
thanks_for_location = "Thanks for 🌏🌎🌍"
