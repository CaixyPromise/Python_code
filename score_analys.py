# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''

import numpy as np
import matplotlib.pyplot as plt

course = ["数学","语文","英语","物理","化学","政治","历史","地理"]
course = np.concatenate((course,[course[0]])) # 闭合
score = [80,95,78,85,45,65,80,60]
data_length = len(score)

angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
score.append(score[0])
angles = np.append(angles,angles[0])
plt.polar(angles, score, "rv--", linewidth = 2)

plt.thetagrids(angles*180/np.pi, course ,fontproperties = "simhei")
plt.fill(angles,score,facecolor = "r",alpha = 0.6)
plt.show()