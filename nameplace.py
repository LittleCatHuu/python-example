#coding=utf-8
Money = 2000
def AddMoney():
    global Money#引用全局变量，关键字global
    Money = Money+1

print(Money)
AddMoney()
print (Money)  

''' 在python中，全局变量一般有两种使用方式：

第一种：是在一个单独的模块中定义好，然后在需要使用的全局模块中将定义的全局变量模块导入。

第二种：直接在当前的模块中定义好，然后直接在本模块中通过global声明，然后使用

Python查找变量是顺序是：先局部变量，再全局变量

第一种：
global_list.py：
    GLOBAL_A='hello'
    GLOBAL_B='world' 
test.py：
    import global_list
    def tt():
        print global_list.GLOBAL_A

    if __name__=='__main__':
        tt()

    #输出：
    hello

第二种：
SOLR_URL='http://solr.org'
def tt():
    global SOLR_URL
    SOLR_URL=SOLR_URL+'#aa'

if __name__=='__main__':
    tt()
    print SOLR_URL

#输出：
http://solr.org#aa'''  