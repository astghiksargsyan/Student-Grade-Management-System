import uuid
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
        username = input("Enter your username: ")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        course = input("Choose the course: ")
        return cls(name, username, password)
    def create_single_student(self):
        tmp = {}
        tmp["student_id"] = self.student_id
        tmp["name"] = self.name
        tmp["username"] = self.username
        tmp["password"] = self.password
        tmp["courses"] = self.courses
        tmp["grades"] = self.grades
        return tmp 


    def __str__(self):
        return (f"Name of the: {self.name} \n"
                f"Username: {self.username} \n"
                f"Courses: {self.courses} \n"
                f"Grades: {self.grades} \n")

