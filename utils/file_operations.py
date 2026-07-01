import json
from models.student import Student
STUDENT_LIST = "data/students.json"
COURSE_LIST = "data/courses.json"
def load_students():
    """Load the students from the file"""
    try:
        with open (STUDENT_LIST, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_to_file(students, student):
    students = load_students()
    students.append(student.create_single_student())
    with open (STUDENT_LIST, "w", encoding="utf-8") as f:
            json.dump(students, f, indent = 4)
def update_student_info(updated_student):
    students = load_students()
    for i, acc in enumerate(students):
        if acc["student_id"] == updated_student["student_id"]:
            students[i] = updated_student
            break
    with open (STUDENT_LIST, "w", encoding="utf-8") as f:
            json.dump(students, f, indent = 4)
def load_courses():
    """Load the courses from the file"""
    try:
        with open (COURSE_LIST, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_course_to_file(courses, course):
    courses = load_courses()
    courses.append(course.create_single_course())
    with open (COURSE_LIST, "w", encoding="utf-8") as f:
            json.dump(courses, f, indent = 4)
