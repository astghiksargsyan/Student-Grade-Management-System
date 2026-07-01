from models.student import Student
from models.course import Course
from utils.file_operations import load_students
from utils.file_operations import save_to_file
from utils.file_operations import update_student_info
from utils.file_operations import load_courses
from utils.file_operations import save_course_to_file
class School:
    #average_performance = 0  
    def __init__(self):
        self.students = load_students()
        self.courses = load_courses()  
        School.total_students = len(self.students)
        School.total_courses = len(self.courses)
    def add_student(self):
        """Registers a new student into the system."""
        student = Student.collect_data()
        print("Student registered successfully!")
        print(student)
        save_to_file(self.students, student)
    def login_function(self):
        """ Authenticates a student using username and password."""
        login_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        for stud in self.students:
            if login_input ==stud["username"] and password_input == stud["password"]:
                print("You have successfully logged in!")
                return stud
        print("Incorrect login details")
    def search_student(self):
        """Searches for a student by name"""
        search_input = input("Enter the name of the student: ")
        for stud in self.students:
            if stud["name"] == search_input: 
                print("*"*25)
                print(f"{stud['name']}\n"
                    f"has the follwoing avialable courses{stud['courses']}\n"
                    f"The grades are: {stud['grades']}\n"
                )
    def load_all_students(self):
        """Displays all available students in the system."""
        for stud in self.students:
            print("*"*25)
            print(f"{stud['name']}\n"
                f"has the follwoing avialable courses{stud['courses']}\n"
                f"The grades are: {stud['grades']}\n"
                )
    def add_course(self):
        """ Adds a new course to the system and saves it to storage."""
        course = Course.collect_course_data()
        save_course_to_file(self.courses, course)
        print("Course successfully added!")
    def view_available_courses(self):
        """Displays all available courses in the system. """
        for course in self.courses:
            print(course)
    
    def assign_grade(self):
        """Assigns a grade to a specific student for a selected course."""
        stud_username_input = input("Enter the username of the student to assign grade: ")
        found = False
        for stud in self.students:
            if stud_username_input == stud["username"]:
                print("Student is found, Enter a course name: ")
                print("Available courses: ")
                for availavle_course in stud["courses"]:
                    print(availavle_course)
                course_input = input("Enter a course to asigne grade: ")
                for course in stud["grades"]:
                    print("courses", course)
                    if course["course"] == course_input:       
                        print("Course is found, Enter a grade: ")
                        try:
                            grade_input = int(input("Enter a grade: "))
                            if School.validate_grade(grade_input):
                                course["grade"] = grade_input
                                break
                        except ValueError:
                            print("Invalid value!! ")
                            
                update_student_info(stud)
                found = True
        if not found:
            print("Student not found")
    @staticmethod
    def validate_grade(grade):
        """Grade validation"""
        if grade >= 0 and grade <= 100:
            return True
        else:
            print("Invlid value")
    def top_students(self):
        """Displays top 3 students based on average grade calculation."""
        sorted_students = sorted(self.students, key=School.avg, reverse=True)

        print("Top 3 students:")
        for stud in sorted_students[:3]:
            print(stud["name"], School.avg(stud))
    
    @staticmethod
    def avg(stud):
        """Calculates the average grade of a student."""
        total = 0
        count = 0
        for g in stud["grades"]:
            for v in g.values():
                total += int(v)
                count += 1
        return total / count if count else 0
    def calculate_gpa(self):
        """calculating gpa"""
        students = self.students
        stud_name = input("Enter a newm of the student: ")
        for stud in students:
            if stud_name == stud["name"]:
                total = 0
                count = 0
                for grade in stud["grades"]:
                    for value in grade.values():
                        total += int(value)
                        count += 1
                if count > 0:
                    average = total / count
                    print(f"{stud['name']}: GPA = {average:.2f}")
                    return f"{stud['name']}: GPA = {average:.2f}"
                else:
                    print(f"{stud['name']} has no grades.")
                    return f"{stud['name']}: GPA = {average:.2f}"

        