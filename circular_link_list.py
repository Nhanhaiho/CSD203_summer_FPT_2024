class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print('ccl is empty')
        else:
            t = self.head
            print(t.data,'-->',end=" ") #the first data --> 
            while t.next != self.head:
                t = t.next
                print(t.data,"-->",end="")
            print(t.next.data)
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node    

    def delete_first(self):
        if self.head is None:
            print('nothing to delete')
        else:
            if self.head == self.tail:
                self.head = None
            else:
                t = self.head
                self.head = t.next
                self.tail.next = self.head
                t = None




L = CLinkList()
n1 = Node(10)
L.head = n1
L.tail = n1
L.tail.next =L.head
# L.display()

n2 = Node(20)
L.tail.next = n2
L.tail = n2
L.tail.next = L.head 

# L.display()

n3 = Node(30)
L.tail.next = n3
L.tail = n3
L.tail.next = L.head

# L.display()

n4 = Node(40)
L.tail.next = n4
L.tail = n4
L.tail.next = L.head

L.display()

L.delete_first()
L.display()