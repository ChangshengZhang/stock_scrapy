#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: merge_data.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com
# Created Time: Sat Nov 25 15:04:25 2017

#########################################################################

import os

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
