class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)
    def display_info(self):
        print(f"student name: {self.name}")
        print(f"student id:{self.student_id}")
        print(f"enrolled courses:")
        for course in self.courses:
            print(f" {course}")


student1 = student("Aml","1")
student1.enroll("programming")
student1.enroll("database")
student1.display_info()
