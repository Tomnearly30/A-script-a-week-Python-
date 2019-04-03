import sys
import random


### get winner###

def fight(x,y):
    if x == y:
       return 0 ### 平局 ###
    elif x == 1:
        if y == 0:
            return 1 ### 电脑赢 ###
        if y == -1:
            return 2 ### 玩家赢 ###
    elif x == 0:
        if y == 1:
            return 2 ### 玩家赢 ###
        if y == -1:
            return 1 ### 电脑赢 ###
    elif x == -1:
        if y == 1:
            return 1 ### 电脑赢 ###
        if y == 0:
            return 2 ### 玩家赢 ###


###main###

a = random.randint(-1,1)

b = int(input("你准备出石头（1)剪刀（0）布（-1):"))


c = ["平局！","你输了！","你赢了！"]
dict = {1:"石头",0:"剪刀",-1:"布"}
print("电脑出的是",dict.get(a))
print("你出的是",dict.get(b))
print(c[fight(a,b)])


