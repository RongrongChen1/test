import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

nums = [1000,  2000,  3000,  4000,  5000,  6000,  7000,  8000,  9000, 10000,]
times = [0.37418699264526367, 1.4212684631347656, 3.246896982192993, 5.931939363479614, 9.122553586959839, 13.025998830795288, 17.94557213783264, 23.20087456703186, 29.737909078598022, 36.50238871574402]
del_time = [0.08377838134765625, 0.3155946731567383, 0.8050220012664795, 1.188232660293579, 1.8642053604125977, 2.5728392601013184, 3.9702789783477783, 4.8900370597839355, 6.836018800735474, 7.909700870513916]

def draw_bar_insert():
    fig,ax=plt.subplots()

    bar1 = plt.bar(range(len(times)),times,color ='blue',alpha = 0.5)

    #给每个柱子上面添加标注
    for b in bar1: #遍历每个柱子
      height = b.get_height()
      value = height
      if height>0: height+=0.3
      else: height = height-2
      ax.annotate('{:.2f}'.format(value),
            #xy控制的是，标注哪个点，x=x坐标+width/2, y=height，即柱子上平面的中间
            xy=(b.get_x() + b.get_width() / 2, height),
            xytext=(0,3), #文本放置的位置，如果有textcoords，则表示是针对xy位置的偏移，否则是图中的固定位置
            textcoords="offset points", #两个选项 'offset pixels'，'offset pixels'
            va = 'bottom', ha = 'center' #代表verticalalignment 和horizontalalignment，控制水平对齐和垂直对齐。
            )


    plt.ylim(ymax = 40)
    plt.xticks(range(len(nums)),nums)
    plt.xlabel("Number of Nodes",size = 13)
    plt.ylabel("Total Time for Inserting Nodes(s)",size = 13)
    plt.show()



def draw_fit_insert():
    fig,ax=plt.subplots()
    def func(x, a, b, c):
        x = x.astype(np.float)
        return a * x * np.log2(b * x) + c

    xdata = np.linspace(1000, 10000, 100)

    popt, pcov = curve_fit(func, np.asarray(nums), np.asarray(times))

    plt.plot(xdata, func(xdata, *popt), 'b-',alpha = 0.5,
             label='%5.3f*x*log_2(x)+%5.3f' % (popt[0],popt[2]))

    i = 0
    for b in nums: #遍历每个柱子
      height = times[i]
      value = height
      if height>0: height+=0.5
      ax.annotate('{:.2f}'.format(value),
            #xy控制的是，标注哪个点，x=x坐标+width/2, y=height，即柱子上平面的中间
            xy=(nums[i] , height),
            xytext=(0,3), #文本放置的位置，如果有textcoords，则表示是针对xy位置的偏移，否则是图中的固定位置
            textcoords="offset points", #两个选项 'offset pixels'，'offset pixels'
            va = 'bottom', ha = 'center' #代表verticalalignment 和horizontalalignment，控制水平对齐和垂直对齐。
            )
      i += 1


    plt.scatter(nums,times)

    plt.legend()
    plt.ylim(ymax = 40)
    # plt.xticks(range(len(nums)),nums)
    plt.xlabel("Number of Nodes",size = 13)
    plt.ylabel("Total Time for Inserting Nodes(s)",size = 13)
    plt.show()


def draw_bar_del(times):
    fig,ax=plt.subplots()

    bar1 = plt.bar(range(len(times)),times,color ='green',alpha = 0.5)

    #给每个柱子上面添加标注
    for b in bar1: #遍历每个柱子
      height = b.get_height()
      value = height
      if height>0: height+=0.3
      else: height = height-2
      ax.annotate('{:.2f}'.format(value),
            #xy控制的是，标注哪个点，x=x坐标+width/2, y=height，即柱子上平面的中间
            xy=(b.get_x() + b.get_width() / 2, height),
            xytext=(0,3), #文本放置的位置，如果有textcoords，则表示是针对xy位置的偏移，否则是图中的固定位置
            textcoords="offset points", #两个选项 'offset pixels'，'offset pixels'
            va = 'bottom', ha = 'center' #代表verticalalignment 和horizontalalignment，控制水平对齐和垂直对齐。
            )

    plt.ylim(ymax = 10)
    plt.xticks(range(len(nums)),nums)
    plt.xlabel("Number of Nodes",size = 13)
    plt.ylabel("Total Time for Delete Top Node",size = 13)
    plt.show()



    draw_bar_insert()


def draw_fit_del(times):
    fig, ax = plt.subplots()

    def func(x, a, b, c):
        x = x.astype(np.float)
        return a * x * np.log2(b * x) + c

    xdata = np.linspace(1000, 10000, 100)

    popt, pcov = curve_fit(func, np.asarray(nums), np.asarray(times))

    plt.plot(xdata, func(xdata, *popt), 'g-', alpha=0.5,
             label='%5.3f*x*log_2(x)+%5.3f' % (popt[0], popt[2]))

    i = 0
    for b in nums:  # 遍历每个柱子
        height = times[i]
        value = height
        if height > 0: height += 0.5
        ax.annotate('{:.2f}'.format(value),
                    # xy控制的是，标注哪个点，x=x坐标+width/2, y=height，即柱子上平面的中间
                    xy=(nums[i], height),
                    xytext=(0, 3),  # 文本放置的位置，如果有textcoords，则表示是针对xy位置的偏移，否则是图中的固定位置
                    textcoords="offset points",  # 两个选项 'offset pixels'，'offset pixels'
                    va='bottom', ha='center'  # 代表verticalalignment 和horizontalalignment，控制水平对齐和垂直对齐。
                    )
        i += 1

    plt.scatter(nums, times,c='g')

    plt.legend()
    plt.ylim(ymax=10)
    # plt.xticks(range(len(nums)),nums)
    plt.xlabel("Number of Nodes", size=13)
    plt.ylabel("Total Time for Deletion of Top Node", size=13)
    plt.show()
# draw_fit()
draw_bar_insert()
draw_fit_insert()
draw_bar_del(del_time)
draw_fit_del(del_time)