# array, linkedlist
# what is stack
#lay ra, them vo, cap nhat, display

#push: insert first
#pop: delete first
#top: return self.head.data 
#  -> return [1], 
# size: 
#display: through 
#sort: 


# linklist implementation by stack

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self):
        data = int(input('enter number to insert into stack: '))
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = None
            self.size += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.size += 1
    
    def pop(self):
        if self.head is None:
            print('empty stack')
            return None
        elif self.head.next is None:
            self.head = None
            self.size -=1
        else:
            t = self.head 
            self.head = t.next
            t = None
            size -=1
        
    def print_size(self):
        return self.size
    
    def print_top_of_stack(self):
        if self.head== None:
            return None
        else:
            return self.head.data
        
    def display_stack(self):
        t = self.head
        if self.head is None:
            print('stack underflow')
        else:
            while t:
                print(t.data)
                t = t.next
            return 

stack = Stack()
stack.push()
stack.push()
stack.push()
stack.display_stack()
top = stack.print_top_of_stack()
print(top)