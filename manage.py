class Student:
    def __init__(self,code,name,mark):
        self.code = code
        self.name =name
        self.mark = mark
class Student_manage:
    def __init__(self):
        self.students = []
        #self.students mot cai list
    def addStu(self,code,name,mark):
        student = Student(code,name,mark)
        #add student using append
        self.students.append(student)
    def show(self):
        if not self.students:
            print('Not found')
        else:
            for student in self.students:
                print(f'code: {student.code}, Name: {student.name}, mark: {student.mark}')
    def delete(self,code):
        for student in self.students:
            if student.code == code:
                self.students.remove(student)
                print(f'Student with code: {code} deleted succesfully!')
                return
        print(f'Student with the code: {code} not found')
    def search(self, name):
        for student in self.students:
            fullName_list = student.name.split()
            for student_name in fullName_list:
                if name in student_name:
                    print(f'found student with name: {student.name},code: {code}, mark: {mark}')
                    break
                else:
                    print('not found')
                    break
    def update(self,code,newName,newMark):
        for student in self.students:
            if student.code == code:
                student.name = newName
                student.mark = newMark
                print(f'student with code: {code} update succesfully! ')
                return
        print(f'can not found student {code}')


#manage

menu = Student_manage()

while True:
    print("\nStudent Menu:")
    print("1. Add Student")
    print("2. Show list of Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Update student by code")
    print("6. Exit")

    choice = input('Enter your choice: ')

    if choice == '1':
        code = input('enter student code: ')
        name =input('enter student name: ')
        mark = float(input('enter student marks: '))
        menu.addStu(code,name,mark)
    elif choice =='2':
        menu.show()
    elif choice =='3':
        name = input('enter your name you want to find: ')
        menu.search(name)
    elif choice =='4':
        code = input('enter your code of student you want to del: ')
        menu.delete(code)
    elif choice =='5':
        code = input('enter your student code you want to find: ')
        newName = input('enter new name: ')
        newMark = input('enter new mark: ')
        menu.update(code,newName,newMark)
    elif choice == '6':
        print('exiting')
        break
    else:
        print('invalid value pls choose from 1 to 6')