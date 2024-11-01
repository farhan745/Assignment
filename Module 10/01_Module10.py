import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\n")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        return self.grades

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print(f"Student {self.name} (ID: {self.student_id}) added successfully.")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course {self.course_name} (Code: {self.course_code}) created with instructor {self.instructor}.")

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter age: "))
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")
    new_student = Student(name, age, address, student_id)
    new_student.display_student_info()
    return new_student

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    course = Course(course_name, course_code, instructor)
    course.display_course_info()
    return course

def enroll_in_course(student, course):
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    student.enroll_course(course.course_name)
    course.add_student(student)
    print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")

def add_grade(student, course):
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    student.add_grade(course.course_name, grade)
    print(f"Grade {grade} added for {student.name} in {course.course_name}.")

def display_student_details(student, course):
    student_id = input("Enter Student ID: ")
    print("Student Information")
    print(f"Name: {student.name}")
    print(f"ID: {student.student_id}")
    print(f"Age: {student.age}")
    print(f"Address: {student.address}")
    print(f"Enrolled Courses: {', '.join(student.courses)}")
    print(f"Grades: {student.grades}")

def display_course_details(course):
    course_code = input("Enter Course Code: ")
    print("Course Information:")
    print(f"Course Name: {course.course_name}")
    print(f"Code: {course_code}")
    print(f"Instructor: {course.instructor}")
    print(f"Enrolled Students: {', '.join([student.name for student in course.students])}")

students = []
courses = []

def save_data():
    data = {
        "students": [
            {
                "name": student.name,
                "age": student.age,
                "address": student.address,
                "student_id": student.student_id,
                "grades": student.grades,
                "courses": student.courses
            } for student in students
        ],
        "courses": [
            {
                "course_name": course.course_name,
                "course_code": course.course_code,
                "instructor": course.instructor,
                "students": [student.student_id for student in course.students]
            } for course in courses
        ]
    }
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("All student and course data saved successfully.")

def load_data():
    global students, courses
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            
            students = []
            for student_data in data["students"]:
                student = Student(student_data["name"], student_data["age"], student_data["address"], student_data["student_id"])
                student.grades = student_data["grades"]
                student.courses = student_data["courses"]
                students.append(student)
            
            courses = []
            for course_data in data["courses"]:
                course = Course(course_data["course_name"], course_data["course_code"], course_data["instructor"])
                course.students = [next(s for s in students if s.student_id == student_id) for student_id in course_data["students"]]
                courses.append(course)
                
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found.")
    except Exception as e:
        print(f"Error loading data: {e}")

while True:
    print("==== Student Management System ====")
    print("1. Add New Student")
    print("2. Add New Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade for Student")
    print("5. Display Student Details")
    print("6. Display Course Details")
    print("7. Save Data to File")
    print("8. Load Data from File")
    print("0. Exit")
    choice = input("Select Option: ")
    if choice == "1":
        x = add_student()
        students.append(x)
    elif choice == "2":
        y = add_course()
        courses.append(y)
    elif choice == "3":
        if students and courses:
            enroll_in_course(students[-1], courses[-1])
        else:
            print("Please add students and courses first.")
    elif choice == "4":
        if students and courses:
            add_grade(students[-1], courses[-1])
        else:
            print("Please add students and courses first.")
    elif choice == "5":
        if students and courses:
            display_student_details(students[-1], courses[-1])
        else:
            print("Please add students and courses first.")
    elif choice == "6":
        if students and courses:
            display_course_details(courses[-1])
        else:
            print("Please add students and courses first.")
    elif choice == "7":
        save_data()
    elif choice == "8":
        load_data()
    elif choice == "0":
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid option, please try again.")
