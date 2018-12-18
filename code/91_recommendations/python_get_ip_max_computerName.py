#! /usr/bin/env python
# -*- coding: utf-8 -*-

# python获取本机MAC地址
import uuid
def get_mac_address():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

import socket
def get_IP_address():
    my_computer_name = socket.getfqdn(socket.gethostname())
    my_ip_address = socket.gethostbyname(my_computer_name)
    print("computer_name: ", my_computer_name)
    print("ip_address:  ", my_ip_address)

print("mac_address: ", get_mac_address())
get_IP_address()

print("----------second idea-----------")
import re,urllib2
class Getmyip:
    def getip(self):
        try:
            print("hahahahah.....")
            myip = self.visit("http://city.ip138.com/ip2city.asp")
            print("hahahahahah.........")
        except:
            try:
                myip = self.visit("http://www.bliao.com/ip.phtml")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                except:
                    myip = "So sorry!!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            print("test........")
            str = opener.read()
            print("str: \n", str)
        return re.search('d+.d+.d+.d+',str).group(0)
getmyip = Getmyip()
localip = getmyip.getip()
print("outter ip: ", localip)
