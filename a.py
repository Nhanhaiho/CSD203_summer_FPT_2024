class IntArr:
    def __init__(self,index,data,capacity):
        self.index=index
        self.data = data
        self.capacity = capacity

    def insert(self,value):
        if self.index < self.capacity:
            if self.index < len(self.data):
                self.data[self.index] = value
            else:
                print('err')
    def delete(self,value):
        for i in range(0,self.index):
            if value == self.data[i]:
                for j in range(i,self.index-1):
                    self.data[j] =self.data[j+1]
                self.data[self.index] = None
                self.index -=1
                return
    def display(self):
        for i in self.data[:self.index]:
            print(i,end=" ")

    def update(self,i,value):
        if i<=self.index:
            self.data[i]= value
    def search(self,value):
        if self.index >0:
            for i in range(self.index):
                if self.data[i]==value:
                    return value

intarr = IntArr(index=0,data=[1,2,3,4],capacity=20)
intarr.insert(5)
intarr.display()