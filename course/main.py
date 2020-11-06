# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from student import Student
from teacher import Teacher

class Course(Teacher):
    def __init__(self, teach_name, age, salary, credit_card, course, title, teacher_name, description, price, max_people_to_enroll, students, student_count, sales, money_earned):
        super().__init__(teach_name, age, salary, credit_card, course)
        self.title = title
        self.teacher_name = teacher_name
        self.description = description
        self.price = price
        self.max_people_to_enroll = max_people_to_enroll
        self.students = []
        self.student_count = float
        self.sales = int
        self.money_earned = float

    def get_students(self):
        return self.students

    def enroll(self):
        if self.student_count < self.max_people_to_enroll:
            return "Enrolling..."
            self.student_count += 1
            self.students.append(Student)
            self.sales += 1
            self.money_earned += self.price
        else:
            return "Class full!"

    def add_course_to_teacher(self):
        if Teacher and self.teacher_name == self.teach_name:
            self.course.append(Course)
        else:
            pass
