# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:47:05 2019

@author: user
"""

from matplotlib.font_manager import FontProperties 
#修正無法顯示中文字體問題

import matplotlib.pyplot as plt
import matplotlib

plt.rcParams['savefig.dpi'] = 150 
plt.rcParams['figure.dpi'] = 150 
matplotlib.rcParams.update({'font.size': 8})

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  #修正設定中文字體
plt.rcParams['axes.unicode_minus'] = False
size = [199089000,28817000,12089000]

labels = '高中及高職教育計畫','一般行政管理計畫','建築及設備計畫'

plt.pie(size, labels = labels,autopct='%1.1f%%')
plt.title('臺北市立南湖高級中學基金用途',fontsize=10,color='r')
plt.show()

