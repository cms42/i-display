# -*- coding: utf-8 -*-
import configparser
import cv2
import sys

if (len(sys.argv)<2) :
    print("usage: ",sys.argv[0]," [config]")
    exit()
if (sys.argv[1] == '--help')|(sys.argv[1] == '-h') :
    print("usage: ",sys.argv[0]," [config]")
    exit()

config = configparser.ConfigParser()
config.read(sys.argv[1])

