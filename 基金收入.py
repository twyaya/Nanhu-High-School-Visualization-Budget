# -*- coding: utf-8 -*
"""
Created on Thu Nov 14 19:05:30 2019

@author: user
"""

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['savefig.dpi'] = 150 
plt.rcParams['figure.dpi'] = 150 
matplotlib.rcParams.update({'font.size': 5})

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
size = [609000,24000,1015000,255000,31132000,2500000,629000]

labels = '服務收入','財產處分收入','租金收入','其他財產收入','學雜費收入','受贈收入','雜項收入'

plt.pie(size, labels = labels,autopct='%1.1f%%')
plt.title('臺北市立南湖高級中學基金來源(已除去公庫撥款收入)',fontsize=10,color='g')
plt.show()

labels = '服務收入','財產處分收入','租金收入','其他財產收入','受贈收入','雜項收入' #除去學雜費收入比較
plt.title('臺北市立南湖高級中學基金來源(已除去公庫撥款、學雜費收入和)',fontsize=10,color='g')
matplotlib.rcParams.update({'font.size': 8})
size = [609000,24000,1015000,255000,2500000,629000]
plt.pie(size, labels = labels,autopct='%1.1f%%')
plt.show()
