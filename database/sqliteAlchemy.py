from sqlalchemy import create_engine # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy import Column, Integer, String # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

engine = create_engine('sqlite:///database.db', echo=True)

Base = declarative_base()

# defining the student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)

# create the students table
Base.metadata.create_all(engine)

# creating a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# inserting some data into the table
student1 = Student(name='Alice', age=20, grade='A')
student2 = Student(name='Bob', age=22, grade='B')
student3 = Student(name='Charlie', age=19, grade='A')

session.add(student1)
session.add(student2)
session.add(student3)
session.commit()

# querying the data from the table
students = session.query(Student).all()
for student in students:
    print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

# filter query
students_with_a_grade = session.query(Student).filter(Student.grade == 'A').all()
for student in students_with_a_grade:
    print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")