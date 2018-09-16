#!/usr/bin/python
#coding:utf8

import os
import logging
import time
from logging.handlers import TimedRotatingFileHandler
base_path = os.getcwd()
log_path = os.path.join(base_path,"log_dis_time")
if not os.path.isdir(log_path):
    os.mkdir(log_path)
log_file = os.path.join(log_path,"log_dis_time.log")
log_formater = '[%(asctime)s] %(levelname)s %(filename)s %(lineno)s %(funcName)s : %(message)s'
log_fromat = logging.Formatter(log_formater)
dis_log = logging.getLogger('my_log')
dis_log.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(filename=log_file,when='M', interval=1, backupCount=3, encoding=None, delay=False)
handler.suffix = "%Y-%m-%d_%H-%M-%S.log"
handler.setFormatter(log_fromat)
dis_log.addHandler(handler)

if __name__ == '__main__':
    while True:
        time.sleep(1)
        dis_log.info("hello world!")
