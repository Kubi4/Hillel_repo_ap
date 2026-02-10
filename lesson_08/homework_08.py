class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def show_info(self):
        print("Name:", self.name, "|", "Surname:", self.surname, "|", "Age:", self.age, "|", "Average Score:", self.average_score)

    def change_average_score(self, new_average_score):
        self.average_score = new_average_score

student_1 = Student("Tom", "Riddle", 17, 95)

student_1.show_info()

student_1.change_average_score(100)

student_1.show_info()

