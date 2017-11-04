#!/usr/bin/python
# File Name: run.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com

#########################################################################

import os
import time

def format_data():

    filename = sorted(os.listdir("holding_data/"))

    flag = 0
    for name in filename:
        
        lines = open("holding_data/"+name).readlines()
        for ii in xrange(1,len(lines)):
            line = lines[ii].split(";")
            code = int(line[0])
            f = open("format_data/"+str(code)+".csv","a")
            tmp = line[2].split(",")
            stock_num = ""
            for ii in tmp:
                stock_num = stock_num + ii
            
            if flag == 0:
                f.write("date;holding_num;holding_perc\n")

            f.write(name.split(".")[0]+";"+stock_num+";"+line[3]+"\n")

        flag = 1

def merge(kk,index):

    print 1

for ii in xrange(1000):

    print "begin run\n"
    os.system("scrapy crawl stock")

    time.sleep(10)
    os.system("rm -rf format_data/*")
    format_data()
    print "done, begin sleep"
    a = 3600*24-10
    time.sleep(a)
