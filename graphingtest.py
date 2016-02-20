# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:44:39 2016

@author: wal
"""

import matplotlib.pyplot as plt
import numpy as np

plt.close()

lines1 = range(0,64,4)
lines2 = [x+68 for x in lines1]

""""
example code for generating color associations
>>> d = {}
>>> d[0] = {}
>>> d[0]['UVA'] = ["#FFFFFF", "#483HFG", "#KF8DH4"]
>>> print d[0]
{'UVA': ['#FFFFFF', '#483HFG', '#KF8DH4']}
>>> print d[0]['UVA']
['#FFFFFF', '#483HFG', '#KF8DH4']
>>> print d[0]['UVA'][0]
#FFFFFF
>>> print len(d[0]['UVA'])
3
>>> 

Options
1. graph individual teams, have a df with wins, sort by lowest, graph those first
2. generate graph with colors on the fly while going through graph
"""

for i in range(0,len(lines1)):
    line_2h = ((lines1[i]+4)+lines2[i])
    line_1h = lines1[i]+4
    #print line_2h
    #print line_1h
    plt.plot((0,1),(line_1h, line_1h), linewidth = 5)
    if i % 2 != 0:
        print i
        if i == 1:
            x_v = i
        plt.plot((x_v,x_v),(lines1[i-1]+4, lines1[i]+4), linewidth = 5)
        mid_point = lines1[i]+4 - ((lines1[i-1]+4 - lines1[i]+4)/2)
        plt.plot((1,2), (mid_point, mid_point), linewidth = 5)
        
        print mid_point
plt.xlim(0,20)
plt.savefig('bracket_test.png', dpi = 300)
    