import uuid
from utils.file_operations import load_courses
from utils.file_operations import load_students

class Student:
    def __init__(self, name, username, password):
        self.student_id = str(uuid.uuid4())
        self.username = username
        self.name = name
        self.password = password
        self.courses = []
        self.grades = []
    @classmethod
    def collect_data(cls):
        """Collect student information from user input."""
        while True:
            username = input("Enter your username: ")
            if cls.is_username_exists(username):
                print("Username already exists. Please choose another one.")
            else:
                break
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        student = cls(name, username, password)
        cls.choose_available_course(student)
        return student
    @staticmethod
    def is_username_exists(username):
        """Prevents using the same username"""
        students = load_students()
        for student in students:
            if student["username"].lower() == username.lower():
                return True
        return False
    @staticmethod
    def password_validation(password):
        pass
    @staticmethod
    def choose_available_course(student):
        courses = load_courses()
        print("Available courses:")
        for course in courses:
            print(course["name"])
        while True:
            course_input = input("Choose the course: ")
            for course in courses:
                if course_input.lower() == course["name"].lower():
                    student.courses.append(course["name"])
                    student.grades.append({
                        "course": course["name"],
                        "credits": course["credits"],
                        "grade": None
                    })
                    print("Course added!")
                    return
            print("Invalid course. Try again.")
    def create_single_student(self):
        """Creates dictionary for working with json files"""
        tmp = {}
        tmp["student_id"] = self.student_id
        tmp["name"] = self.name
        tmp["username"] = self.username
        tmp["password"] = self.password
        tmp["courses"] = self.courses
        tmp["grades"] = self.grades
        return tmp 
    def __str__(self):
        """Return a human-readable string representation of the student."""
        return (f"Name of the: {self.name} \n"
                f"Username: {self.username} \n"
                f"Courses: {self.courses} \n"
                f"Grades: {self.grades} \n")

    def __repr__(self):
        """Return the official string representation of student."""
        return f"Student({self.username}, {self.name})"

