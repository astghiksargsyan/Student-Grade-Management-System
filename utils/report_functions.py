STUDENT_LIST = "data/students.json"
COURSE_LIST = "data/courses.json"
REPORT = 'data/report.txt'
from models.school import School
school = School()
def gra_report():
    reported_student = school.calculate_gpa()
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("School Report\n")
        f.write("*" * 25 + "\n")
        f.write(f"Number of courses: {School.total_courses}\n")
        f.write(f"Number of students: {School.total_students}\n\n")
        f.write(reported_student)
