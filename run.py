#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: run.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com

#########################################################################

import os
import time
import sys

def format_data():

    filename = sorted(os.listdir("holding_data/"))

    flag = 0
    for name in filename:
        
        lines = open("holding_data/"+name).readlines()
        for ii in xrange(1,len(lines)):
            line = lines[ii].split(";")
            code = str(int(line[0]))
            for kk in xrange(4-len(code)):
                code = "0"+code

            f = open("format_data/"+code+"_"+line[1].strip(" ")+".csv","a")
            tmp = line[2].split(",")
            stock_num = ""
            for ii in tmp:
                stock_num = stock_num + ii
            
            if flag == 0:
                f.write("date,holding_num,holding_perc\n")

            f.write(name.split(".")[0]+","+stock_num.strip(" ")+","+line[3].strip(" "))

        flag = 1

def merged(kk,index):

    filename = sorted(os.listdir("format_data/"))

    output_lines = []
    header = "stock_id,stock_name"
    flag = 0
    for stock_num in filename:

        output = stock_num.split('.')[0]
        output = output.split("_")
        output = output[0]+".hk"+","+output[1].split(",")[0]
        lines = open("format_data/"+stock_num).readlines()
        for ii in xrange(1,len(lines)):
            line = lines[ii].split(",")
            if flag == 0:
                header = header + "," + line[0]
            output = output +"," +line[kk].strip("\n")
        output_lines.append(output+"\n")
        flag = 1
    f = open("output/"+index+".csv","w")
    f.write(header+"\n")
    f.writelines(output_lines)


def final_merged():

    output_num_lines = []
    output_perc_lines = []
    for file_name in sorted(os.listdir("format_data")):

        stock_id = file_name[0:4]+".hk"
        content = open("format_data/"+file_name).readlines()
        date_line = "date"
        stock_num_line = stock_id 
        stock_perc_line = stock_id
        for ii in xrange(1,len(content)):
            tmp_line = content[ii].strip("\n").split(",")
            date_line = date_line+","+tmp_line[0]
            stock_num_line = stock_num_line+","+tmp_line[1]
            stock_perc_line = stock_perc_line +"," +tmp_line[2]

        if len(output_num_lines) == 0:
            output_num_lines.append(date_line+"\n")
        if len(output_perc_lines) == 0:
            output_perc_lines.append(date_line+"\n")

        output_num_lines.append(stock_num_line +"\n")
        output_perc_lines.append( stock_perc_line + "\n")

    f = open("output_data/stock_num.csv","w")
    f.writelines(output_num_lines)
    f.close()

    f = open("output_data/stock_perc.csv","w")
    f.writelines(output_perc_lines)
    f.close()


for ii in xrange(1000):

    print "begin run\n"
    os.system("scrapy crawl stock")

    time.sleep(10)
    os.system("rm -rf format_data/*")
    format_data()
    time.sleep(10)
    merged(1,"hold_num")
    merged(2,"hold_perc")

    print "done, begin sleep"
    a = 3600*24-30
    time.sleep(a)
