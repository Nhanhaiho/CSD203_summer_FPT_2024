class Student():
    def __init__(self,student_id,name,mark):
        self.student_id = student_id
        self.name = name
        self.mark = mark
        self.next = None
class Link_list():
    def __init__(self):
        self.head = None

    def insert_first(self,student_id,name,mark):
        new_node = Student(student_id,name,mark)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self,student_id,name,mark):
        new_node = Student(student_id,name,mark)
        if not self.head:
            self.head = new_node
            return 
        t = self.head
        while t.next:
            t = t.next
        t.next = new_node


    def remove_first(self):
        if not self.head:
            print('list is empty can not delete')
            return
        self.head = self.head.next
        

    def remove_last(self):
        if not self.head:
            print('list is empty can not delete')
            return
        if not self.head.next:
            self.head = None
            return
        t = self.head
        while t.next is not None:
            preNode = t
            t = t.next
        preNode.next = None
        

    def remove_by_id(self,id):
        if not self.head:
            print('list is empty')
            return
        if self.head.student_id == id:
            self.head = self.head.next
            return
        t = self.head
        while t:
            if t.next.student_id == id:
                t.next = t.next.next
                return
            t = t.next
        print(f'student with id: {student_id} not found')


    def search_by_name(self,name):
        if not self.head:
            print('list is empty. No student found')
            return
        flag = False
        t = self.head
        while t:
            if name.lower() in t.name.lower():
                print('student found')
                print(t.name,t.student_id,t.mark)
                flag = True
            t = t.next
        if not flag:
            print(f'student with id: {name} not found')

    def search_by_id(self,id):
        pass
    def update_by_id(self,id):
        pass
    def display_info(self):
        if not self.head:
            print('empty')
            return
        t = self.head 
        while t:
            print(t.name,t.student_id,t.mark)
            t = t.next
        


def display_menu():
    print("\n================================")
    print("\nMenu:")
    print("1. Insert a student at begin")
    print("2. Insert a student at end")
    print("3. remove first student ")
    print("4. remove last student ")
    print("5. remove students by id")
    print("6. Search by name")
    print("7. Search by id")
    print("8. Update by id")
    print("9. Display information")

if __name__ == "__main__":
    students = Link_list()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice =="1":
            name = input("Enter your student's name: ")
            student_id = int(input('Enter student id: '))
            marks = float(input("enter student marks: "))
            students.insert_first(name,student_id,marks)
        elif choice =="2":
            name = input("Enter your student's name: ")
            student_id = int(input('Enter student id: '))
            marks = float(input("enter student marks: "))
            students.insert_last(name,student_id,marks)
        elif choice =="3":
            students.remove_first()
        elif choice =="4":
            students.remove_last()
        elif choice =="5":
            id_to_del = int(input("Enter a studnet id you want to del: "))
            students.remove_by_id(id_to_del)
        elif choice =="6":
            name_to_search = input('enter a name you want to search: ')
            students.search_by_name(name_to_search)
        elif choice =="9":
            students.display_info()
        elif choice =="10":
            print('exiting...')
            break
        else: print('invalid choice. Pls try again')



        