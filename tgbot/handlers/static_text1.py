start_created = "Привет, {first_name}!"
start_not_created = "И снова привет, {first_name}!"
start_intro = "Меня зовут Inbaze, и я портфолио-бот 🤖\n" \
              "Я помогаю отслеживать рост / падение твоего инвестиционного портфеля 📊, " \
              "и в будущем буду писать если что-то растет или падает больше чем на 10%"
start_currency = "Давай выберем валюту, в которой будем считать твой портфель"
start_currency_dollar_text = 'USD 💵'
start_currency_euro_text = 'EUR 💶'
start_currency_button_answer_button = 'Супер! Сохранил {currency} как основную 💪'
start_trade_experience = 'Расскажи теперь про свой подход к инвестициям? 💼'
start_trade_experience_yes_text = 'Активно торгую, постоянно что-то докупаю / продаю. Вхожу в спекулятивные активы'
start_trade_experience_no_text = 'Пассивный игрок. Не важно падает или растет - держу до победного'
start_trade_experience_button_answer_yes_button = 'Понял, надеюсь бот будет полезен'
start_trade_experience_button_answer_no_button = 'Понял. В будущем мы добавим периодические рекомендации ' \
                                                 'покупки / продажи. Возможно будет полезно.'
start_trade_experience_recommendation_text = 'Также на основании состояния рынка, в будущем я планирую давать ' \
                                             'тебе рекомендации по трейдингу.'
start_help_tune_portfolio_text = 'Если хочешь, могу провести экскурсию по тому что я умею сейчас 🧑‍💻'
start_help_tune_portfolio_question_text = 'Эксурсия или сам разберешься?'
start_help_yes_text = 'Давай'
start_help_no_text = 'Спасибо, я сам'
start_help_button_answer_yes_button = 'Окей, в первую очередь выставим твой портфель 💼:' \
                                      ' добавим акции / криптомонеты, которыми уже владеешь' \
                                      ' и сколько ты готов инвестировать в будущем (нужно для рекомендаций) '
start_help_button_answer_no_button = 'Как знаешь 🐰 \n' \
                                     'Если что, команды можешь вызвать через слэш(/).️'
start_important_to_invest_text = 'ВАЖНО: Баланс "Готов инвестировать" показывает сумму, которую ты готов ' \
                                 'проинвестировать и в зависимости от его размера я буду лучше понимать какие советы ' \
                                 'тебе давать.'
start_write_portfolio_command_text = 'Выбери команду /portfolio (👈 или просто нажми на неё)'

# portfolio
wait_for_portfolio = 'Имей терпение - это может занять несколько минут. \n\n' \
                     'Чем больше портфель - тем больше собирать по нему информацию 🤓\n'
your_portfolio = 'Твое портфолио - показывает кто ты на самом деле:\n\n'
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
                              'Если захочешь повторить наш разговор - жми или пиши /start\n' \
                              'Если захочешь взглянуть на портфель еще раз - жми или пиши: /portfolio'
close_modify_menu_nested_after_start = 'Так, ну что же - мы познакомились с функционалом ведения портфолио' \
                                       ' с чем тебя и поздравляю.\n\n' \
                                       'Остальной функционал(рекомендации, уведомления и тд) сейчас находятся' \
                                       ' в режиме разработки и пока недоступны.\n\n' \
                                       ' А теперь прошу тебя сказать наколько тебе зашел сам' \
                                       ' бот на данный момент по шкале от 1-5(где 1 - безразично, а 5 очень интересно' \
                                       'и давно искал что-то подобное)? '
mark_1 = '1'
mark_2 = '2'
mark_3 = '3'
mark_4 = '4'
mark_5 = '5'

answer_on_mark = 'В любом случае - благодарю за оценку!\n\n' \
                 'Если захочешь повторить наш разговор - жми или пиши /start\n' \
                 'Если захочешь взглянуть на портфель еще раз - жми или пиши: /portfolio'

change_balance_text = 'Введи cимвол акции / криптомонеты, баланс которого ты бы хотел ИЗМЕНИТЬ' \
                      '(допустим у Microsoft символы - "MSFT", а у биткоина к доллару - "BTC-USD")\n' \
                      'а если нужно поменять средства которые ты бы готов инветсировать просто нажми кнопку 👇'
add_stock_text = 'Введи cимвол акции / криптомонеты, который ты бы хотел ДОБАВИТЬ ' \
                 '(допустим у Tesla - символы TSLA, а у биткоина к доллару - "BTC-USD").\n' \
                 'Ну или вернись назад если ошибся кнопкой👇'
delete_stock_text = 'Введи cимвол акции / криптомонеты, который ты бы хотел УДАЛИТЬ из портфеля ❌\n' \
                    'ВАЖНО: удалишь актив и вся информация по нему будет удалена из твоего портфолио ' \
                    'без возможности возврата ❗️\n' \
                    '(допустим у Tesla - символы TSLA, а у биткоина к доллару - "BTC-USD").\n' \
                    'Ну или вернись назад если ошибся кнопкой👇'

modify_to_invest_button = '"Готов инвестировать" изменить'
back_to_modify_button = '🔙 Назад'

change_balance_text_stock_write = 'Значит его МЕНЯЕМ, хорошо'
delete_stock_write = 'Значит его УДАЛЯЕМ, хорошо'
add_stock_write = 'Значит такой тикет ДОБАВЛЯЕМ, хорошо'

modify_wrong_ticket = 'Попробуй ввести еще раз)\nСимволы которые можно применять: a-z, A-Z, 0-9, . и -.\n' \
                      'Кол-во символов: 3-6.'
add_wrong_ticket = 'Попробуй ввести еще раз)\nСимволы которые можно применять: a-z, A-Z, 0-9, . и -.\n' \
                   'Кол-во символов: 3-6.'
delete_wrong_ticket = 'Попробуй ввести еще раз)\nСимволы которые можно применять: a-z, A-Z, 0-9, . и -.\n' \
                      'Кол-во символов: 3-6.'

modify_balance_stock_not_in_portfolio = 'Такого тикета нет в твоем портфолио или его в принципе не существует\n' \
                                        'Если первый вариант - добавь тикер в предыдущем меню 🔙\n' \
                                        'пересмотри наименование тикера еще раз тут https://finance.yahoo.com '
modify_balance_stock_symbol_shares = 'У тебя в 💼 сейчас {shares} акций {symbol}.\n А сколько должно быть? (пиши цифрами' \
                                     'в таком формате:\nЕсли 2 акции / криптомонеты пишешь - "2", ' \
                                     'если 2,53 пишешь - "2.53")\n\n' \
                                     'БЕЗ КАВЫЧЕК и ЧЕРЕЗ ТОЧКУ ЕСЛИ НЕ ЦЕЛОЕ ЧИСЛО!'
delete_stock_info = 'У тебя в 💼 сейчас {shares} акций / криптомонет {symbol}.\n' \
                    'Ты действительно хочешь удалить эту акцию / криптомонету из своего портфеля?'
delete_stock_success = 'Ты успешно распрощался с {symbol} в твоем портфеле, надеюсь выгодно ушла🙏'
delete_stock_cancel = 'Значит не продаем {symbol}, хорошо'
delete_stock_yes_text = 'Удалить 🗑'
delete_stock_no_text = 'Оставить ❤️'

modify_balance_stock_shares_success = 'Обновили количесво акций!\nТеперь у тебя {shares} акций {stock}\n' \
                                      'А теперь введи сколько всего ты потратил на приобретение всех акций / криптомонет' \
                                      ' этого тикета?\n\n ' \
                                      'Конечно в той валюте которую ты указал изначально и если хочешь считать' \
                                      ' до копеек то делай это через точку, пожалуйста.\n\n' \
                                      'Пример на: 100 долларов и 27 центов - 100.27'
modify_balance_stock_total_costs_success = 'Обновили общее количество затраченных тобой средств на приобритение данных ' \
                                           'акций / криптомонет!\n' \
                                           'Ты потратил {total_costs} на покупку{shares} акций / криптомонет{stock}\n'

change_to_invest_text = 'У тебя сейчас: {to_invest}\n' \
                        'Какая должна быть новая сумма?'
changed_to_invest_text = 'Cупер! Я обновил твой баланс и теперь он равен: {to_invest}\n'

add_stock_symbol_check_already_have = 'У тебя уже есть эта позиция ({symbol}) в размере {shares}.\n\n' \
                                      'Если хочешь изменить его баланс - иди в меню изменений (кнопка под' \
                                      ' портфолио "Поменять", а затем "✏️ Изменить баланс️").'
add_stock_symbol_check_success = 'Мы с тобой успешно добавили {symbol} тебе в 💼.\n' \
                                 'Теперь напиши сколькими акциями / криптомонетами ты обладаешь?\n\n(пиши цифрами ' \
                                 'в таком формате:\nЕсли 2 акции пишешь - "2", если 2,53 пишешь - "2.53")\n\n' \
                                 'БЕЗ КАВЫЧЕК и ЧЕРЕЗ ТОЧКУ ЕСЛИ НЕ ЦЕЛОЕ ЧИСЛО!'
add_stock_not_in_yfinance = 'Такого тикета нет в твоем портфолио или его в принципе не существует\n' \
                            'пересмотри наименование тикера еще раз тут https://finance.yahoo.com '

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

github_button_text = 'GitHub'
secret_level_button_text = 'Секретный уровень'