# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:26:30 2016

@author: Connor
"""
import pdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 15})
mpl.rcParams['axes.facecolor'] = 'white'


#colors = pd.read_csv('colors.csv')
#
#
#id_ns = set(list(colors['ID']))
#
#
#for i in range(0,len(id_ns)):
"""
I need to start laying some ground rules on this thing.

1. If the only other color is white ( or grey as may be), then make the line
 have the : linestyle in white to give it some definition maybe, can try other ways as well as I go.

2.  




  
"""    
import matplotlib.pyplot as plt
import itertools

# put all the linestyles you want in the list below (non exhaustive here)
style=itertools.cycle(["-","--","-.",":",".","h","H"])

lstyles = ["-","--","-.",":",".","h","H"]
lstyless = ["a","b","c","d","e","f","g"]
x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]
q = [2,3,4,5,6,7,8,9,10,11]
# assuming xseries and yseries previously created (each one is a list of lists)

z =[3,4,5,6,7,8,9,10,11,12]
c = [4,5,6,7,8,9,10,11,12,13]
m = [5,6,7,8,9,10,11,12,13,14]


       
#plt.plot(x,y, linewidth = 5, linestyle = ':', color = "#FFFFFF")
plt.plot(x,y, linewidth = 8, linestyle = '-', color = "#1B4178")#,
       #  path_effects=[path_effects.SimpleLineShadow(offset = (3,-3),shadow_color = "g"),
                     #  path_effects.Normal()])
plt.plot(x,y, linewidth = 8, linestyle = '--', color = "#F5873C")

plt.plot(x,z, linewidth = 8, linestyle = '-', color = "#EE9627")#,
       #  path_effects=[path_effects.SimpleLineShadow(offset = (3,-3),shadow_color = "g"),
                     #  path_effects.Normal()])
#plt.plot(x,z, linewidth = 6, linestyle = '.-', color = "white")


plt.plot(x,q, linewidth = 8, linestyle = '-', color = "#A82B3D")#,
       #  path_effects=[path_effects.SimpleLineShadow(offset = (3,-3),shadow_color = "g"),
                     #  path_effects.Normal()])
#plt.plot(x,q, linewidth = 6, linestyle = '.-', color = "white")

plt.plot(x,c, linewidth = 8, linestyle = '-', color = "#1C453A")
plt.plot(x,c, linewidth = 6, linestyle = '--', color = "#1C453A")

plt.plot(x,m, linewidth = 8, linestyle = '-', color = "#EA4B0F")
plt.plot(x,m, linewidth = 8, linestyle = '--', color = "#00204E")

plt.plot(x,z, linewidth = 8, linestyle = '-', color = "#00539C")


plt.show()#('test.png', dpi = 600)


    
    