﻿# -*- coding: utf-8 -*-

import sys
import thread
from socket import *

def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        lock.acquire()
        print "Open Port:",port
        lock.release()


if __name__=='__main__':
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])
    target_ip = gethostbyname(host)
    lock = thread.allocate_lock()
    for port in range(start_port, end_port):
        thread.new_thread(tcp_test, (port,))