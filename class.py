#coding=utf-8
class A(object): 
    def __method(self): 
        print (self) 
    def method(self): 
        self.__method() 
        
a = A() 
a.method()