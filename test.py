import config
import telebot
import sw





bot = telebot.TeleBot(config.token)

@bot.message_handler(regexp='^/vlan_info')
def info_o_vlan_sw(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, 'ОПА!')

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, message.text)
        print(message)




if __name__ == '__main__':
    bot.polling(none_stop=True)
