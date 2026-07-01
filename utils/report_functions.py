import json
STUDENT_LIST = "data/students.json"
COURSE_LIST = "data/courses.json"
REPORT = 'data/report.txt'
from models.school import School

school = School()
from utils.file_operations import load_students
def count_students():
    students = load_students
    with open(REPORT, "w") as f:
        f.write(f"Number of students in school {str(len(students))}")

def gra_report():
    students = load_students()
    reported_student = school.calculate_gpa()
    with open(REPORT, "w") as f:
        f.write(f"Number of students in school {reported_student}")
