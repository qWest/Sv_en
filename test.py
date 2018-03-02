import config
import telebot
import sw





bot = telebot.TeleBot(config.token)

@bot.message_handler(regexp='^/vlan_info')
def info_o_vlan_sw(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, 'ОПА!')


@bot.message_handler(regexp='^/chvlan 172\.16\.21\.\d{2,3} \d(1,2)')
def chandge_vlan(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, 'меняю VLAN...')
        bot.send_message(config.owner_id, str(message.from_user.id)+'\n'+str(message.text))


@bot.message_handler(regexp='^/chvlan')
def chandge_vlan(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, 'фигню пишешь.')
        bot.send_message(config.owner_id, str(message.from_user.id)+'\n'+str(message.text))

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, message.text)
        print(message)




if __name__ == '__main__':
    bot.polling(none_stop=True)
