class Node:
    def __init__(self,id,name,mark):
        self.id = id
        self.name = name
        self.mark = mark
        self.next = None
        self.prev = None

class DoubleLinkList:
    def __init__(self):
        self.head = None
    
    def insert_first(self,id,name,mark):
        new_student = Node(id,name,mark)
        if self.head is None:
            self.head = new_student
        else:
            new_student.next = self.head
            self.head.prev = new_student
            self.head = new_student
            print(f'insert new student with id:{id}, name: {name}, mark: {mark} at the start of the list')

    def insert_last(self,id,name,mark):
        new_student = Node(id,name,mark)
        if self.head is None:
            self.head = new_student
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = new_student
            new_student.prev = t
            print(f'insert new student with id:{id}, name: {name}, mark: {mark} at the last of the list')

    def delete_first(self):
        if not self.head:
            print('list is empty')
            return 
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            print('list is empty')
            return 
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.prev.next = None

    def delete_by_id(self, id):
        t = self.head
        while t:
            if t.id == id:
                if t.prev:
                    t.prev.next = t.next
                if t.next:
                    t.next.prev = t.prev
                if t ==self.head:
                    self.head = t.next
                print(f'delete with id: {t.__delattr__id}')
                return
            t = t.next
    print(f'can not find id: {id}')

    def search_by_id(self, id):
        t = self.head
        while t :
            if t.id == id:
                print(f'found student with id: {t.id}')
                return 
            t = t.next
        print(f'student with id: {id} not found')

    def search_by_name(self,name):
        t = self.head
        flag = False
        while t:
            if name in t.name.lower():
                print(f'found student with name: {t.name}, id: {t.id}, mark: {t.mark} ')
                flag = True
            t = t.next
        if not flag:
            print('not found')

    def update_by_id(self,id,new_name,new_mark):
        student_to_update = self.search_by_id(id)
        if student_to_update:
            student_to_update.name = name
            student_to_update.mark = mark
            print(f'updated student with id: {id} with new name: {new_name} and new mark: {new_mark}')
        else:
            print(f'not found student with id: {id}')
    
    def display(self):
        t = self.head
        if not t:
            print('list is empty')
            return 
        print('---------------student list----------------')
        while t :
            print(f'student id: {t.id} , name: {t.name} , mark: {t.mark}')
            t = t.next 



def menu():
    dll = DoubleLinkList()
    while True:
        print('\nMenu')
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Delete First")
        print("4. Delete Last")
        print("5. Delete by ID")
        print("6. Search by Name")
        print("7. Search by ID")
        print("8. Update by ID")
        print("9. Display")
        print("0. Exit")
        choice = int(input('enter your choice: '))

        if choice == 1:
            id = input('enter student id: ')
            name = input('Enter student name: ')
            mark = float(input('Enter student mark: '))
            dll.insert_first(id,name,mark)
        elif choice == 2:
            id = input('enter student id: ')
            name = input('Enter student name: ')
            mark = float(input('Enter student mark: '))
            dll.insert_last(id,name,mark)
        elif choice == 3:
            ddl.delete_last()
        elif choice == 4:
            ddl.delete_last()
        elif choice == 5:
            id_to_del = input('Enter id you want to delete: ')
            dll.delete_by_id(id_to_del)
        elif choice == 6:
            name = input('Enter name to search: ')
            dll.search_by_name(name)
        elif choice == 7:
            id = inpuut('Enter id you want to find to see full info: ')
            dll.search_by_id(id)
        elif choice == 8:
            id = inpuut('Enter id you want to')
            new_name = input('Enter new name: ')
            new_mark = float(input('Enter new mark:'))
            dll.update_by_id(id,new_name,new_mark)
        elif choice == 9:
            dll.display()
        elif choice == 0:
            break
        else:
            print('pls choose choice from 0 - 9, try again')

if __name__ == '__main__':
    menu()