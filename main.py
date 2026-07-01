from utils.report_functions import  gra_report
from models.school import School

school = School()

init_options = (
    ("1", "Login", school.login_function),
    ("2", "Register", school.add_student),  # this is an add student
    ("3", "Search Student", school.search_student),
    ("4", "Filter Students", school.top_students),
    ("5", "View Students", school.load_all_students), 
    ("6", "Calculate Average Grades", school.calculate_gpa),
    ("7", "View Available Courses", school.view_available_courses),
    ("8", "Add Course",school.add_course),
    ("9", "Assign Grade", school.assign_grade),
    ("10", "Create Report", gra_report),
)
def main():
    print("*"*25) 
    print("Choose from the available options")
    print("*"*25) 
    for id, name, __ in init_options:
        print(f"{id}: {name}")
    start_input = input("Enter the corresponding value: ")
    for id, __,  funct in init_options:
        if start_input == id:
            funct()
            return
    print("Invalid option. Please try again.")
main()