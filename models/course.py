import uuid
class Course:
    def __init__(self, course_code, name, credits):
        self.course_code = str(uuid.uuid4())
        self.name = name
        self.credits = credits
    @classmethod
    def collect_course_data(cls):
        course_name_input = input("enter a course name")
        course_credits = input("enter a course credits")
        return cls(
            course_code=None,
            name=course_name_input,
            credits=course_credits
        )
    def create_single_course(self):
        tmp = {}
        tmp["course_code"] =self.course_code
        tmp["name"] = self.name
        tmp["credits"] = self.credits
        return tmp
    def __str__(self):
        return (
            f"{self.course_code}\n"
            f"{self.name}\n"
            f"{self.credits}\n"
        )
    def __repr__(self):
        return self.__str__()