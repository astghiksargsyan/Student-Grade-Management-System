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
        """Return a human-readable string representation of the studnet."""
        return (f"Name of the: {self.name} \n"
                f"Username: {self.username} \n"
                f"Courses: {self.courses} \n"
                f"Grades: {self.grades} \n")

    def __repr__(self):
        """Return the official string representation of student."""
        return self.__str__()

