# -*- coding: utf-8 -*-
import configparser
import cv2
import sys
import socket
import os.path
import logging
import time

if (len(sys.argv)<2) :
    print("usage: ",sys.argv[0]," [config]")
    exit()
if (sys.argv[1] == '--help')|(sys.argv[1] == '-h') :
    print("usage: ",sys.argv[0]," [config]")
    exit()

config = configparser.ConfigParser()
config.read(sys.argv[1])

logger = logging.getLogger()
if bool(config["server"]["debug"]) :
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/logs/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='a')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info('started')

addr = ((config["server"]["host"]),int(config["server"]["port"]))
max_client_num = int(config["server"]["max_client_num"])
tctime = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tctime.bind(addr)
tctime.listen(max_client_num)

