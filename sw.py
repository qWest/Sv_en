import telnetlib
import time

def sw_login(sw_telnet):
    sw_telnet.write(b'admin\n')
    sw_telnet.write(b'xxx')
    time.sleep(1)
    sw_output = sw_telnet.read_very_eager().decode('utf-8').split('\n')
    sw_inv = sw_output[len(sw_output) - 1]
    return(sw_inv)

def sw_model(sw_telnet,sw_inv):
    sw_telnet.write(b'sh sw\n')
    sw_output = sw_telnet.read_until(bytes(sw_inv,"utf8")).decode('utf-8').split('\n')
    print(sw_output)

def sw_conf(sw_telnet,sw_inv):
    sw_telnet.write(b'conf t\n')
    time.sleep(1)
    sw_telnet.write(b'passwords aging 0\n')
    sw_telnet.write(b'sntp server 192.168.125.58 poll\n')
    time.sleep(1)
    sw_telnet.write(b'exit\n')
    sw_telnet.write(b'write\n')
    time.sleep(3)
    sw_output = sw_telnet.read_very_eager().decode('utf-8')
    print(sw_output)
    sw_telnet.write(b'y\n')
    sw_output = sw_telnet.read_until(bytes(sw_inv, "utf8")).decode('utf-8')
    print(sw_output)


#for i in range(254):
#    try:
#        telnet = telnetlib.Telnet(ip_net+str(i+1),23,5)
#        inv = sw_login(telnet)
#    except:
#        print('Error'+str(i+1))
#        continue
#    sw_conf(telnet,inv)
#    print(inv+' + '+str(i+1))
#    telnet.close()
