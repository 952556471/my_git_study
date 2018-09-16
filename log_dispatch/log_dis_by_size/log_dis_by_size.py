#!/usr/bin/python
#coding:utf8

import logging
from logging.handlers import RotatingFileHandler
import os
base_path = os.getcwd()
print("base_path:%s"%base_path)

log_dir = "by_size_log"
log_dir_path = os.path.join(base_path,log_dir)
print("log_dir_path:%s"%log_dir_path)

#创建日志文件夹
if not os.path.isdir(log_dir):
    os.makedirs(log_dir_path)

log_file_name = os.path.join(log_dir_path,"dis_log_file.log")
log_formater = '[%(asctime)s] %(levelname)s %(filename)s %(lineno)s %(funcName)s : %(message)s'
logging.basicConfig(level=logging.NOTSET,
                format=log_formater)
log_format = logging.Formatter(log_formater)
dis_log = logging.getLogger("log_dis_by_size")
dis_log.setLevel(logging.NOTSET)

log_handler = RotatingFileHandler(filename=log_file_name,maxBytes=1024*10,backupCount=5)
log_handler.setFormatter(log_format)
dis_log.addHandler(log_handler)

if __name__ == '__main__':
    for _ in range(10000):
        dis_log.debug("hello world!")
















