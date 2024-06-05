class Student:
    def __init__(self,student_id,name,mark):
        self.student_id = student_id
        self.name = name
        self.mark = mark
        self.next = None

class LinkedList:
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
            print(t.name, t.stu_id, t.mark)
            t = t.next
        t.next = new_node

    def display_student(self):
        t = self.head
        while t:
            print(t.name,t.student_id,t.mark)
            t = t.next

    def delete_first(self):
        if not self.head:
            print('list is empty can not delete')
            return
        self.head = self.head.next
    def delete_last(self):
        if not self.head:
            print("List is empty. No node to delete.")
            return
        if not self.head.next:
            self.head = None
            return
        t = self.head
        preNode = None
        while t.next is not None:
            preNode = t
            t = t.next
        preNode.next = None

    def delete_by_id(self,student_id):
        if not self.head:
            print("List is empty. No node to delete.")
            return
        if self.head.student_id == student_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.student_id == student_id:
                current.next = current.next.next
                return
            current = current.next
        print("Student with ID" ,student_id, "not found.")
    def seacrh_by_name(self,name):
        if not self.head:
            print('list is empty. No student found')
            return
        flag = False
        t = self.head
        while t:
            if name.lower() in t.name.lower():
                print('student found')
                print(t.name, t.student_id, t.mark)
                flag = True
            t = t.next
        if not flag :
            print(f'student containing:{name} can not found')
    def search_by_id(self,student_id):
        if not self.head:
            print('empty list, not found')
            return
        t = self.head
        while t:
            if t.student_id ==student_id:
                print('student found')
                print(t.name,t.student_id,t.mark)
                return
        print(f"student with {student_id} not found")
    def update_by_id(self,student_id,new_name,new_mark):
        if not self.head:
            print('list is empty')
            return
        t = self.head
        while t:
            if t.student_id == student_id:
                t.name = new_name
                t.mark=new_mark
                print('Updated')
                return
            t = t.next


def display_menu():
    print("\nMenu:")
    print("1. Insert a student at the beginning")
    print("2. Insert a student at the end")
    print("3. Display list")
    print("4. Delete a student at the beginning")
    print("5. Delete a student at the end")
    print("6. Delete a student by id ")
    print("7. Search by name")
    print("8. Search by id")
    print("9. Update by id")
    print("10. EXIT")

if __name__ == "__main__":
    students = LinkedList()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = int(input("Enter student ID: "))
            marks = float(input("Enter student marks: "))
            students.insert_first(name, student_id, marks)
        elif choice == "2":
            name = input("Enter student name: ")
            student_id = int(input("Enter student ID: "))
            marks = float(input("Enter student marks: "))
            students.insert_last(name, student_id, marks)
        elif choice == "3":
            print("Student List:")
            students.display_student()
        elif choice =="4":
            students.delete_first()
        elif choice =="5":
            students.delete_last()
        elif choice == "6":
            id = int(input("Enter student ID: "))
            students.delete_by_id(id)
        elif choice =="7":
            name = input('enter a name you want to find: ')
            students.seacrh_by_name(name)
        elif choice =="8":
            student_id = int(input('enter id you want to search: '))
            students.search_by_id(student_id)
        elif choice =="9":
            id = int(input('enter id you want to update: '))
            new_name = input('enter new name: ')
            new_marks = float(input('enter new mark: '))
            students.update_by_id(id,new_name,new_marks)
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")