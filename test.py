class Student:
    def __init__(self, student_id, name, mark):
        self.student_id = student_id
        self.name = name
        self.mark = mark

    def __repr__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Mark: {self.mark}"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CCL:
    def __init__(self):
        self.last = None

    def insert_first(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def print_list(self):
        if self.last is None:
            print('empty list')
            return
        current = self.last.next
        while True:
            print(current.data)
            current = current.next
            if current == self.last.next:
                break

    def delete_first(self):
        if self.last is None:
            print('no data found')
            return
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def delete_last(self):
        if self.last is None:
            print('no data found')
            return
        if self.last.next == self.last:
            self.last = None
        else:
            current = self.last.next
            while current.next != self.last:
                current = current.next
            current.next = self.last.next
            self.last = current

    def delete_by_id(self, student_id):
        if self.last is None:
            return
        current = self.last.next
        prev = self.last
        while True:
            if current.data.student_id == student_id:
                if current == self.last:
                    if self.last.next == self.last:
                        self.last = None
                    else:
                        prev.next = current.next
                        self.last = prev
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.last.next:
                break

    def search_by_name(self, name):
        if self.last is None:
            return None
        current = self.last.next
        while True:
            if name in current.data.name:
                print(current.data)
            current = current.next
            if current == self.last.next:
                break

    def search_by_id(self, student_id):
        if self.last is None:
            return None
        current = self.last.next
        while True:
            if current.data.student_id == student_id:
                return current.data
            current = current.next
            if current == self.last.next:
                break
        return None

    def update_by_id(self, student_id, name=None, mark=None):
        student = self.search_by_id(student_id)
        if student:
            if name is not None:
                student.name = name
            if mark is not None:
                student.mark = mark
            print(f"Updated student: {student}")
        else:
            print(f"Student with ID {student_id} not found.")

def menu():
    ccl = CCL()
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
            ccl.insert_first(student)
        elif choice == 2:
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            mark = input("Enter student mark: ")
            student = Student(student_id, name, mark)
            ccl.insert_last(student)
        elif choice == 3:
            ccl.delete_first()
        elif choice == 4:
            ccl.delete_last()
        elif choice == 5:
            student_id = input("Enter student ID to delete: ")
            ccl.delete_by_id(student_id)
        elif choice == 6:
            name = input("Enter student name to search: ")
            ccl.search_by_name(name)
        elif choice == 7:
            student_id = input("Enter student ID to search: ")
            student = ccl.search_by_id(student_id)
            if student:
                print(student)
            else:
                print(f"Student with ID {student_id} not found.")
        elif choice == 8:
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (or press Enter to skip): ")
            mark = input("Enter new mark (or press Enter to skip): ")
            name = name if name else None
            mark = mark if mark else None
            ccl.update_by_id(student_id, name, mark)
        elif choice == 9:
            ccl.print_list()
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
