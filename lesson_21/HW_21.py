# 1. Створення моделі даних
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import random


engine = create_engine("postgresql://postgres:Postgresql123@localhost/postgres")

Base = declarative_base()

student_course = Table("student_course",Base.metadata,Column("student_id", Integer, ForeignKey("students.id")),Column("course_id", Integer, ForeignKey("courses.id")))

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Course", secondary=student_course, back_populates="students")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship("Student", secondary=student_course, back_populates="courses")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

courses = [
    Course(title="Python"),
    Course(title="Java"),
    Course(title="SQL"),
    Course(title="JS"),
    Course(title="QA")
]

session.add_all(courses)
session.commit()

names = [f"Student {i}" for i in range(1, 21)]

all_courses = session.query(Course).all()

for name in names:
    student = Student(name=name)
    student.courses = random.sample(all_courses, random.randint(1, 3))
    session.add(student)

session.commit()

# 2. Виконання базових операцій
new_student = Student(name="New Student 21")

python_course = session.query(Course).filter_by(title="Python").first()

new_student.courses.append(python_course)

session.add(new_student)
session.commit()

# 3. Запити до бази даних
# 3.1 Запит до бази даних, який повертає інформацію про студентів, зареєстрованих на курс Python

course = session.query(Course).filter_by(title="Python").first()
print('Студенти курсу Python:')
for student in course.students:
    print(student.name)

# 3.2 Запит до бази даних, який повертає інформацію про курси, на які зареєстрований студент 4

student = session.query(Student).filter_by(name="Student 4").first()
print('---------------------------------')
print('Курси студента 4:')
for course in student.courses:
    print(course.title)

# 4. Оновлення та видалення даних
# 4.1 Функція для оновлення ім'я студента
def update_student(student_name, new_name):
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        student.name = new_name
        session.commit()
    else:
        print("Student not found")

update_student("Student 15", "Updated Student 15")

# 4.2 Функція для оновлення назви курсу
def update_course(course_title, new_title):
    course = session.query(Course).filter_by(title=course_title).first()

    if course:
        course.title = new_title
        session.commit()
    else:
        print("Course not found")

update_course("Python", "Python Advanced")

#4.3 Функція для видалення студента
def delete_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()

    if student:
        session.delete(student)
        session.commit()
    else:
        print("Student not found")

delete_student("Student 8")
