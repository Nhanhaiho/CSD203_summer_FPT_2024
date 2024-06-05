import ctypes
from random import randint

class Dynamic_Arr:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.elements = self.makeArr(self.capacity)

    def makeArr(self,capacity):
        return (ctypes.py_object *capacity)()

    def showInfor(self):
        print('actual size: ',self.size)
        print('capacity: ',self.capacity)
        for i in range(self.size):
            print(self.elements[i])

    def resize(self,size):
        b = self.makeArr(size) #tao lai 1 arr
        for i in range(self.size): #lap qua arr co san
            b[i] = self.elements[i] #lay thong tin cua arr cũ append vao het arr b[i]
        self.elements = b #mang moi co gia tri la b
        self.capacity = size

    def append(self,value):
        if self.size ==self.capacity: #neu ma mang day
            self.resize(self.capacity*2) # thay doi kich thuoc bang cach nhan doi mang len 2 lan
        self.elements[self.size]= value # mang o vi tri size se dc gan value ng dung nhap
        self.size +=1

    def insert(self,index,value):
        if self.size ==self.capacity:
            self.resize(2*self.capacity) # resize lai cho mang tang gap doi kich thuoc
            #sau do chay qua mang
        for j in range(self.size,index,-1):
            self.elements[j] = self.elements[j-1] # xe dich cac phan tu trong mang qua phai mot don vi
        self.elements[index] = value #gan gia tri can insert vao vi tri mong muon
        self.size +=1



    def removeByIndex(self,index):
        if index < self.size:
            for j in range(index,self.size-1):
                self.elements[j] =self.elements[j+1]
            self.elements[self.size-1] = None
            self.size-=1
        else:
            print('not found')

    def removeByValue(self,value):
        for i in range(self.size):
            if self.elements[i] == value:  # tim thay dc phan tu can xoa
                for j in range(i,self.size-1):
                    self.elements[j]  =self.elements[j+1]
                self.elements[self.size-1] = None
                self.size -=1
                return
            raise ValueError('Value not found')


obj = Dynamic_Arr()
obj.showInfor()
for i in range(3):
    obj.append(randint(0,10))
obj.showInfor()
obj.insert(2,30)
obj.showInfor()

