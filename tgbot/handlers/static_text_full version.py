start_created = "Привет, {first_name}!"
start_created_2nd_string = 'Если хочешь перейти к портфелю - жми или пиши: /portfolio'
start_not_created = "И снова привет, {first_name}!"
start_intro = "Меня зовут Inbaze и я портфолио-бот 🤖\n" \
              "Я помогаю отслеживать рост / падение твоего инвестиционного портфеля 📊." \
              " В будущем буду писать, если что-то растет или падает больше, чем на 10%"
start_currency = "Давай выберем валюту, в которой будем считать твой портфель"
start_currency_dollar_text = 'USD 💵'
start_currency_euro_text = 'EUR 💶'
start_currency_button_answer_button = 'Супер! Сохранил {currency} как основную 💪'
start_trade_experience = 'Теперь расскажи про свой подход к инвестициям? 💼'
start_trade_experience_yes_text = 'Активно торгую, постоянно что-то докупаю / продаю. Вхожу в спекулятивные активы'
start_trade_experience_no_text = 'Пассивный игрок. Неважно, падает или растет - держу до победного'
start_trade_experience_button_answer_yes_button = 'Понял, надеюсь бот будет полезен'
start_trade_experience_button_answer_no_button = 'Понял. В будущем мы добавим периодические рекомендации' \
                                                 ' покупки / продажи. Возможно, будет полезно.'
start_trade_experience_recommendation_text = 'На основании состояния рынка я буду давать' \
                                             ' рекомендации по покупке / продаже активов. Но это в будущем.'
start_help_tune_portfolio_text = 'Если хочешь, могу провести экскурсию и показать, что я умею 🧑‍💻'
start_help_tune_portfolio_question_text = 'Эксурсия или сам разберешься?'
start_help_yes_text = 'Давай'
start_help_no_text = 'Спасибо, я сам'
start_help_button_answer_yes_button = 'Окей, в первую очередь подготовим твой портфель 💼:' \
                                      ' добавим акции / криптомонеты, которыми уже владеешь,' \
                                      ' и выделим сумму, которую ты готов инвестировать в будущем' \
                                      ' (нужно для рекомендаций)'
start_help_button_answer_no_button = 'Как знаешь 🐰 \n' \
                                     'Если что, команды можешь вызвать через слэш(/).️'
start_important_to_invest_text = 'ВАЖНО: Баланс "Готов инвестировать" это сумма, которую ты готов' \
                                 ' вложить в ближайшем будущем. В зависимости от его размера я буду лучше понимать,' \
                                 ' какие рекомендации давать.'
start_write_portfolio_command_text = 'Выбери команду /portfolio 👈'

# portfolio
wait_for_portfolio = 'Терпение - это может занять несколько минут. \n\n' \
                     'Чем больше портфель - тем больше собирать по нему информацию 🤓\n'
your_portfolio = 'Твое портфолио показывает, кто ты на самом деле:\n\n'
to_invest_text = 'Готов инвестировать'
total_portfolio = 'Текущая стоимость'
net_profit_button = 'Чистый доход'
total_profit_button = 'Итог'
costs_button = 'Затраты'
efficiency_button = '%'
amount_button = 'Кол-во'
update_button = 'Обновить'

wait_update = 'Портфолио обновляется ⏱ - может занять пару минут.'

modify_button = 'Поменять'
modify_question = 'Что менять?'

balance_button = '✏️ Поменять баланс'
add_stock_button = '➕ Добавить акцию / криптомонету'
delete_stock_button = '➖ Убрать акцию / криптомонету'
close_button = '❌ Ничего'
close_modify_menu_portfolio = 'Понял, удаляюсь.\n\n' \
                              'Если захочешь повторить диалог - жми или пиши /start\n' \
                              'Если захочешь взглянуть на портфель еще раз - жми или пиши: /portfolio'
close_modify_menu_nested_after_start = 'Ну что же, мы познакомились с функционалом ведения портфолио,' \
                                       ' с чем тебя и поздравляю.\n\n' \
                                       'Остальной функционал(рекомендации, уведомления и тд) сейчас находятся' \
                                       ' в режиме разработки и пока недоступны.\n\n' \
                                       ' А теперь прошу тебя сказать, наколько тебе полезен' \
                                       ' бот на данный момент по шкале от 1-5(где 1 - безразично, а 5 - очень' \
                                       ' интересно и давно искал что-то подобное)?'
mark_1 = '1'
mark_2 = '2'
mark_3 = '3'
mark_4 = '4'
mark_5 = '5'

answer_on_mark = 'В любом случае - благодарю за оценку!\n\n' \
                 'Если захочешь повторить диалог - жми или пиши /start\n' \
                 'Если захочешь взглянуть на портфель еще раз - жми или пиши: /portfolio'

change_balance_text = 'Введи cимвол акции / криптомонеты, баланс которой хочешь ИЗМЕНИТЬ' \
                      ' (допустим у Microsoft символ - "MSFT", а у биткоина к доллару - "BTC-USD").\n' \
                      'Если ошибься - вернись назад через кнопку 🔙'
add_stock_text = 'Введи cимвол акции / криптомонеты, которую хочешь ДОБАВИТЬ' \
                 ' (допустим у Tesla - символ TSLA, а у биткоина к доллару - "BTC-USD").\n' \
                 'Если ошибся - вернись назад через кнопку 🔙'
delete_stock_text = 'Введи cимвол акции / криптомонеты, которую хочешь УДАЛИТЬ из портфеля ❌\n' \
                    'ВАЖНО: Вся информация по нему будет удалена из твоего портфолио' \
                    ' без возможности возврата ❗️\n' \
                    '(допустим у Tesla - символ TSLA, а у биткоина к доллару - "BTC-USD").\n' \
                    'Если ошибся - вернись назад через кнопку 🔙'

modify_to_invest_button = 'Поменять баланс будущих инвестиций'
back_to_modify_button = '🔙 Назад'

change_balance_text_stock_write = 'МЕНЯЕМ, хорошо'
delete_stock_write = 'УДАЛЯЕМ, хорошо'
add_stock_write = 'ДОБАВЛЯЕМ, хорошо'

modify_wrong_ticket = 'Попробуй ввести еще раз)\nСимволы которые можно применять: a-z, A-Z, 0-9, . и -.\n' \
                      'Кол-во символов: 3-6.'
add_wrong_ticket = 'Попробуй ввести еще раз)\nСимволы которые можно применять: a-z, A-Z, 0-9, . и -.\n' \
                   'Кол-во символов: 3-6.'
delete_wrong_ticket = 'Попробуй ввести еще раз)\nСимволы которые можно применять: a-z, A-Z, 0-9, . и -.\n' \
                      'Кол-во символов: 3-6.'

modify_balance_stock_not_in_portfolio = 'Ошибка: либо этой позиции нет в портфеле, либо ее в принципе не существует\n' \
                                        'Если первый вариант - добавь тикер через "добавить акцию / криптомонету" 🔙\n' \
                                        'Если второй вариант - посмотри название тикера тут https://finance.yahoo.com '
modify_balance_stock_symbol_shares = 'В портфеле сейчас {shares} акций {symbol}.\n На сколько изменяем? \n' \
                                     '(Пример 2 акции - "2",2,53 - "2.53"), \n\n'
delete_stock_info = 'В портфеле сейчас {shares} акций / криптомонет {symbol}.\n' \
                    'Ты действительно хочешь удалить эту акцию / криптомонету из своего портфеля?'
delete_stock_success = 'Ты удалил {symbol} с портфеля, надеюсь выгодно ушла🙏'
delete_stock_cancel = 'Не продаем {symbol}, хорошо'
delete_stock_yes_text = 'Удалить 🗑'
delete_stock_no_text = 'Оставить ❤️'

modify_balance_stock_shares_success = 'Обновили количесво акций!\nТеперь у тебя {shares} акций {stock}\n' \
                                      'Введи, какая сумма потрачена на покупку этого кол-во акций / криптомонет?\n\n' \
                                      'Пример: 100 долларов и 27 центов - 100.27'
modify_balance_stock_total_costs_success = 'Обновил количество потраченных денег!\n' \
                                           'Итог: потрачено {total_costs} на покупку{shares} акций / криптомонет{' \
                                           'stock}\n '

change_to_invest_text = 'У тебя сейчас: {to_invest}\n' \
                        'Какой будет новая сумма?'
changed_to_invest_text = 'Cупер! Я обновил твой баланс, и теперь он равен: {to_invest}\n'

add_stock_symbol_check_already_have = 'У тебя уже есть позиция ({symbol}) в размере {shares}.\n\n' \
                                      'Если хочешь изменить баланс - выбери "Поменять баланс будущих инвестиций️"' \
                                      'в /portfolio).'
add_stock_symbol_check_success = '{symbol} успешно добавлен в портфель.\n' \
                                 'Укажи количество акций / криптомонет, которыми владеешь?\n\n(Пример 2 акции - "2", ' \
                                 '2,53 - "2.53")\n\n'
add_stock_not_in_yfinance = 'Ошибка: либо этой позиции нет в портфеле, либо ее в принципе не существует\n' \
                            'Если первый вариант - добавь тикер через "добавить акцию / криптомонету" 🔙\n' \
                            'Если второй вариант - посмотри название тикера тут https://finance.yahoo.com '

# дальше не трогаем

broadcast_command = '/broadcast'

broadcast_no_access = "Sorry, you don't have access to this function."
broadcast_header = "This message will be sent to all users.\n\n"
confirm_broadcast = "Confirm✅"
decline_broadcast = "Decline❌"
message_is_sent = "Message is sent✅\n\n"
declined_message_broadcasting = "Message broadcasting is declined❌\n\n"

error_with_markdown = "Can't parse your text in Markdown style."
specify_word_with_error = " You have mistake with the word "

secret_admin_commands = "⚠️ Secret Admin commands\n" \
                        "/stats - bot stats"

not_admin_answer = "You are not a admin!"

unlock_secret_room = "Congratulations! You've opened a secret room👁‍🗨. There is some information for you:\n" \
                     "*Users*: {user_count}\n" \
                     "*24h active*: {active_24}"

share_location = "Would you mind sharing your location?"
thanks_for_location = "Thanks for 🌏🌎🌍"