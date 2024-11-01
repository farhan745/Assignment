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

        print(f"Student {self.name} (ID: {self.student_id})added successfully.")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(
            f"Course {self.course_name} (Code: {self.course_code}) created with instructor {self.instructor}."
        )


  



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


def enroll_in_course(new_student, course):
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")

    print(
        f"Student {new_student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code})."
    )


def add_grade(new_student, course):
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    grades = new_student.add_grade(course.course_name, grade)
    print(f"Grade {grade} added for {new_student.name} in {course.course_name}.")
    return grades


def display_student_details(new_student, course, grade):
    student_id = input(("Enter Student ID: "))
    print("Student Information")
    print(f"Name: {new_student.name}")
    print(f"ID: {new_student.student_id}")
    print(f"Age: {new_student.age}")
    print(f"Address: {new_student.address}")
    print(f"Enrolled Courdes: {course.course_name}")
    print(f"Grades: {grade}")


def display_course_details(new_student, course):
    course_code = input(("Enter Course Code: "))
    print("Course Information:")
    print(f"Course Name: {course.course_name}")
    print(f"Code: {course_code}")
    print(f"Instructor: {course.instructor}")
    print(f"Enrolled Students: {new_student.name}")
    students = []
    courses = []
def save_data(new_student,cour):
        data = { "students": 
          [ {
            "name": new_student.name,
            "age": new_student.age,
            "address": new_student.address,
            "student_id": new_student.student_id,
            "grades": new_student.grades,
            "courses": new_student.courses }
            ],
          "courses": [
            { "course_name": cour.course_name,
             "course_code": cour.course_code,
             "instructor": cour.instructor,
             } ]
        }
        with open('data.json', 'w') as f:
          json.dump(data, f, indent=4)
        print("All student and course data saved successfully.")
def load_data():
    global students, courses
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            
            for student_data in data["students"]:
                # Create student object without grades and courses
                student = Student(student_data["name"], student_data["age"], student_data["address"], student_data["student_id"])
                # Manually set the grades and courses
                student.grades = student_data["grades"]
                student.courses = student_data["courses"]
                students.append(student)

            for course_data in data["courses"]:
                course = Course(course_data["course_name"], course_data["course_code"], course_data["instructor"])
                # Recreate student enrollment in courses
                course.students = [next(s for s in students if s.student_id == student_id) for student_id in course_data["students"]]
                courses.append(course)

        print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data file not found.")
    except Exception as e:
        print(f"Error loading data: {e}")

# Assuming the rest of your code remains the same



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

    elif choice == "2":
        y = add_course()

    elif choice == "3":
        enroll_in_course(x, y)
    elif choice == "4":
        grade = add_grade(x, y)
    elif choice == "5":
        display_student_details(x, y, grade)
    elif choice == "6":
        display_course_details(x, y)
    elif choice == "7":
        save_data(x,y)
    elif choice == "8":
        load_data()
    elif choice == "0":
       print("Exiting Student Management System. Goodbye!")
       break
    else:
        print("Invalid")
