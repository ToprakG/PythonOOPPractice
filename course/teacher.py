class Teacher:
    def __init__(self, teach_name, age, salary, credit_card, course):
        self.teach_name = teach_name
        self.age = age
        self.salary = salary
        self.credit_card = credit_card
        self.course = []

    def get_name(self):
        return self.name