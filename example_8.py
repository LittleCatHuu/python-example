#coding=utf-8
'''题目：暂停一秒输出。'''

import time

data = {1:'a',2:'b',3:'c'}
for key in data:
    print key,data[key]
    time.sleep(1)   #pause 1s

for key,value in dict.items(data):
    print key,value
    time.sleep(2)    