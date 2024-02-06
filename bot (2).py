import telebot

# Замените 'YOUR_BOT_TOKEN' на полученный от BotFather токен
bot = telebot.TeleBot('5722657450:AAFO0r0qhMWKzzTLOQPMpRYDoLX6tWA1DwI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Замените 'path/to/your/file.txt' на путь к файлу, который вы хотите отправить
    file_path = 'C:/Users/Саша/Desktop/bot/test.ods'
    
    try:
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
            bot.send_message(message.chat.id, "Здравствуйте! Добро пожаловать в наш бот! Табличный файл выше - Наш прайслист. Скачайте его, заполните и отправьте обратно в эту переписку. После обработки заказа, наш менеджер свяжется с вами")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Что-то пошло не так... Подождите пару минут, мы уже разбираемся.")

# Ловим сообщения с файлами от пользователей
@bot.message_handler(content_types=['document'])
def handle_document(message):
    # Пересылаем файл в чат с вашим ID (замените на свой ID)
    bot.forward_message('971491385', message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Спасибо за отправленный файл! Скоро наш менеджер свяжется с вами!")

# Запускаем бота
bot.polling(none_stop=True)