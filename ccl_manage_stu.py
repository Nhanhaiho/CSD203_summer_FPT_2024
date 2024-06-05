class Student:
    def __init__(self,student_id,name,mark):
        self.student_id = student_id
        self.name = name
        self.mark = mark

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CCL:
    def __init__(self):
        self.last = None
        self.head = None
# 1
    def insert_first(self,data):
        new_node = Node(data)
        if self.last is None:
            self.last= new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node
# 2
    def insert_last(self,data):
        new_node = Node(data)
        if self.last is None:
            self.last= new_node
            return
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
# 3
    def print_list(self):
        if self.head is None:
            print('empty list')
        else:
            t = self.head
            while t.next != self.head:
                t = t.next
                print(t.data)
            print(t.next.data)
# 4
    def delete_first(self):
        if self.head is None:
            print('no data found')
        else:
            if self.head == self.tail:
                self.head = None
            else:
                t = self.head
                self.head = t.next
                t = None
                self.tail.next = self.head
# 5
    def delete_last(self):
        if self.head is None:
            print('no data found')
        else:
            if self.head == self.tail:
                self.head = None
            else:
                t = self.head
                while t.next != self.tail:
                    t = t.next
                self.tail = None
                self.tail = t
                t.next = self.head
# 6
    def delete_by_id(self,id):
        if self.last ==None:
            return
        t = self.last.next
        while t != self.last:
            if t.data.id ==id:
                break
            t = t.next
# 7
    def search_by_name(self,name):
        if self.last == None:
            return None
        t = self.last
        while t != self.last:
            if name in t.data.names:
                return t.data
            t = t.next
        if name in t.data.names:
            return t.data
        return None
# 8
    def search_by_student_id(self, student_id):
        if self.last is None:
            return None
        t = self.last.next 
        while True:
            if t.last.data.student_id == student_id:
                return t.data
            t = t.next
            if t == self.last.next:
                break
        return None

# 9
    def update_by_id(self, student_id):
        student = self.search_by_student_id(student_id)
        if student:
            if name is not None:
                student.name = name
            if mark is not None:
                student.mark = mark
            print('updated successfully')
        else:
            print(f'not found student with id: {student.id}')

        
        # menu for user to choose
def menu():
    function = CCL()
    while True:
        print("\nMenu:")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Delete First")
        print("4. Delete Last")
        print("5. Delete by ID")
        print("6. Search by Name")
        print("7. Search by ID")
        print("8. Update by ID")
        print("9. Print List")
        print("10. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            mark = input("Enter student mark: ")
            student = Student(student_id, name, mark)
            function.insert_first(student)
        elif choice ==2:
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            mark = input("Enter student mark: ")
            student = Student(student_id, name, mark)
            function.insert_last(student)
        elif choice == 3:
            function.delete_first()
        elif choice == 4:
            function.delete_last()
        elif choice ==5:
            student_id = input("Enter student id: ")
            function.delete_by_id(student_id)
        elif choice ==6:
            name = input('enter name to search: ')
            function.search_by_name(name)
        elif choice ==7:
            student_id = input('Enter student id to search: ')
            function.search_by_student_id(student_id)
        elif choice ==8:
            student_id = input('Enter student id: ')
            new_name = input('Enter new name: ')
            new_mark = input('Enter new mark: ')
            function.update_by_student_id(student_id, new_name, new_mark)
        elif choice ==9:
            function.print_list()
        elif choice ==10:
            break
        else:
            print('OUT OF CHOICES, pls choose from 1-10')

if __name__ == "__main__":
    menu()

        