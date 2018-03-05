import config
import telebot
import telnetlib
import sw
import time





bot = telebot.TeleBot(config.token)

@bot.message_handler(regexp='^/infovlan')
def info_o_vlan_sw(message):
    if message.chat.id in config.good_ids:
        bot.send_message(message.chat.id, 'ОПА!')


@bot.message_handler(regexp='^/rubvlan')
def chandge_vlan(message):
    if message.chat.id in config.good_ids:
        split_cmd = message.text.split()
        print(split_cmd)
        if len(split_cmd)==3 and split_cmd[1] in config.good_sw_ud and split_cmd[2] in config.good_sw_port:
            fst_msg = bot.send_message(message.chat.id,'Переключаю VLAN')
            try:
                telnet = telnetlib.Telnet(split_cmd[1], 23, 5)
            except:
                bot.send_message(message.chat.id, 'Коммутатор не отвечает')
                return()

            inv = sw.sw_login(telnet)
            telnet.write(b'conf t\n')
            time.sleep(1)
            telnet.write(bytes('int fa1/0/'+split_cmd[2]+'\n',"utf8"))
            time.sleep(1)
            telnet.write(b'sw acc vlan 1507\n')
            time.sleep(1)
            telnet.write(b'no service-acl input\n')
            telnet.write(b'service-acl input not_PPPOE_pck_lock_1507\n')
            time.sleep(1)
            telnet.write(b'exit\n')
            telnet.write(b'exit\n')
            time.sleep(1)
            telnet.write(b'write\n')
            time.sleep(3)
            sw_output = telnet.read_very_eager().decode('utf-8')
            print(sw_output)
            telnet.write(b'y\n')
            sw_output = telnet.read_until(bytes(inv, "utf8")).decode('utf-8')
            print(sw_output)
            telnet.close()
            bot.edit_message_text('Готово!\nКоммутатор '+inv+'\nIP '+split_cmd[1]+'\nПорт '+split_cmd[2]+'\nПереключен на Рубиком', fst_msg.chat.id, fst_msg.message_id)
            #bot.send_message(message.chat.id, 'Готово!\nКоммутатор '+inv+'\nIP '+split_cmd[1]+'\nПорт '+split_cmd[2]+'\nПереключен на Рубиком')

        else:
            bot.send_message(message.chat.id, 'Некорректный ввод данных')
        bot.send_message(config.owner_id, str(message.from_user.id)+'\n'+str(message.text))

@bot.message_handler(regexp='^/aksvlan')
def chandge_vlan(message):
    if message.chat.id in config.good_ids:
        split_cmd = message.text.split()
        print(split_cmd)
        if len(split_cmd)==3 and split_cmd[1] in config.good_sw_ud and split_cmd[2] in config.good_sw_port:
            fst_msg = bot.send_message(message.chat.id,'Переключаю VLAN')
            try:
                telnet = telnetlib.Telnet(split_cmd[1], 23, 5)
            except:
                bot.send_message(message.chat.id, 'Коммутатор не отвечает')
                return()

            inv = sw.sw_login(telnet)
            telnet.write(b'conf t\n')
            time.sleep(1)
            telnet.write(bytes('int fa1/0/'+split_cmd[2]+'\n',"utf8"))
            time.sleep(1)
            telnet.write(b'sw acc vlan 1505\n')
            time.sleep(1)
            telnet.write(b'no service-acl input\n')
            telnet.write(b'service-acl input not_PPPOE_pck_lock\n')
            time.sleep(1)
            telnet.write(b'exit\n')
            telnet.write(b'exit\n')
            time.sleep(1)
            telnet.write(b'write\n')
            time.sleep(3)
            sw_output = telnet.read_very_eager().decode('utf-8')
            print(sw_output)
            telnet.write(b'y\n')
            sw_output = telnet.read_until(bytes(inv, "utf8")).decode('utf-8')
            print(sw_output)
            telnet.close()
            bot.edit_message_text('Готово!\nКоммутатор ' + inv + '\nIP ' + split_cmd[1] + '\nПорт ' + split_cmd[2] + '\nПереключен на Аксиому', fst_msg.chat.id, fst_msg.message_id)
            #bot.send_message(message.chat.id, 'Готово!\nКоммутатор '+inv+'\nIP '+split_cmd[1]+'\nПорт '+split_cmd[2]+'\nПереключен на Аксиому')

        else:
            bot.send_message(message.chat.id, 'Некорректный ввод данных')
        bot.send_message(config.owner_id, str(message.from_user.id)+'\n'+str(message.from_user.first_name)+' '+str(message.from_user.last_name)+'\n'+str(message.text))


if __name__ == '__main__':
    bot.polling(none_stop=True)
