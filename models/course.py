import uuid
class Course:
    def __init__(self, course_code, name, credits):
        self.course_code = str(uuid.uuid4())
        self.name = name
        self.credits = credits
    @classmethod
    def collect_course_data(cls):
        """Collect course information from user input."""
        course_name_input = input("Enter the course name: ")
        while True:
            try:
                course_credits = int(input("Enter the course credits: "))
                if cls.validate_credits(course_credits):
                    break
            except ValueError:
                print("Please enter a valid number.")
        return cls(
            course_code=None,
            name=course_name_input,
            credits=course_credits
        )
    @staticmethod
    def validate_credits(credits):
        """Validate that course credits are positive."""
        if  credits > 0 and credits <= 100:
            return True
        else:
            print("Please enter a number between 0 - 100")
    def create_single_course(self):
        """Creates dictionary for working with json files"""
        tmp = {}
        tmp["course_code"] =self.course_code
        tmp["name"] = self.name
        tmp["credits"] = self.credits
        return tmp
    def __str__(self):
        """Return a human-readable string representation of the course."""
        return (
            f"Course Code: {self.course_code}\n"
            f"Course Name: {self.name}\n"
            f"Credits: {self.credits}"
        )     
    def __repr__(self):
        """Return the official string representation of the course."""
        return self.__str__()