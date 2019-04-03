import sys
import random


def random1to100():
    return random.randint(1,100)

### main ###

a = random1to100()


b = int(input("我在1到100之间选择了一个数，你有5次机会，猜猜看吧:"))

if a == b:
    print("哇塞，第一次就猜对了！"),sys.exit()
elif a > b:
  print("比我选的数小了，还有4次机会，再猜")
else:
  print("比我选的数大了，还有4次机会，再猜")

c = int(input("第2次猜测:"))

if a == c:
    print("这次你猜对了！"),sys.exit()
elif a > c:
  print("比我选的数小了，还有3次机会，再猜")
else:
  print("比我选的数大了，还有3次机会，再猜") 

d = int(input("第3次猜测:"))
if a == d:
    print("这次你猜对了！"),sys.exit()
elif a > d:
  print("比我选的数小了，还有2次机会，再猜")
else:
  print("比我选的数大了，还有2次机会，再猜")

e = int(input("第4次猜测:"))

if a == e:
    print("这次你猜对了！"),sys.exit()
elif a > e:
  print("比我选的数小了，还有最后1次机会，再猜")
else:
  print("比我选的数大了，还有最后1次机会，再猜")

f = int(input("第5次猜测:"))

if a == f:
    print("你终于猜对了！"),sys.exit()
else:
  print("我选的是", a), print("胜败乃兵家常事，大侠请重新来过！")
