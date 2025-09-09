from sqlalchemy import Column,Integer,String,ForeignKey,Table,create_engine
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base = declarative_base()

# Association table for many-to-many relationship between Student and Course
student_course = Table(
        'student_course',
        Base.metadata,
        Column('student_id', Integer, ForeignKey('students.id')),
        Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
        __tablename__ = 'students'
        id = Column(Integer,primary_key=True)
        name = Column(String)

        courses = relationship('Course', secondary=student_course, back_populates='students')

class Course(Base):
        __tablename__ = 'courses'
        id = Column(Integer,primary_key=True)
        title = Column(String)

        students = relationship('Student', secondary=student_course, back_populates='courses')

# Database setup
engine = create_engine('sqlite:///relationship3.db')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()