# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:47:05 2019

@author: user
"""

from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['savefig.dpi'] = 150 
plt.rcParams['figure.dpi'] = 150 
matplotlib.rcParams.update({'font.size': 8})

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
size = [199089000,28817000,12089000]

labels = '高中及高職教育計畫','一般行政管理計畫','建築及設備計畫收入'

plt.pie(size, labels = labels,autopct='%1.1f%%')
plt.title('臺北市立南湖高級中學基金用途',fontsize=10,color='r')
plt.show()

