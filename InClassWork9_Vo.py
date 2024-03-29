#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:27:10 2024

@author: tandyllc
"""
class Course:
    def __init__(self, name, code, max_students):
        self.name = name
        self.code = code
        self.max_students = max_students
        self.enrolled_students = []
        self.prereqs = []
    
    def add_student(self, student):
        if len(self.enrolled_students) < self.max_students:
            print(f"Enrolling {student.name} in {self.name}")
            for course_code in self.prereqs:
                print(f"Checking if {student.name} finished {course_code}")
                for finished_course in student.finished_courses:
                    if finished_course.code == course_code:
                        self.enrolled_students.append(student.name)
                        print(f"{student.name} meets the prerequisites for {self.name}.")
            if self.prereqs == []:
                self.enrolled_students.append(student.name)

            return True
        else:
            return False
        
    def is_full(self):
        return len(self.enrolled_students) >= self.max_students
    
    def add_prerequisites(self, prereq_course_code):
        self.prereqs.append(prereq_course_code.code)
        
    def get_prerequisites(self):
        return self.prereqs
    
    def get_enrolled_students(self):
        return self.enrolled_students

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []
        self.finished_courses = []
    
    def enroll(self, course):
        if course.add_student(self):
            self.enrolled_courses.append(course.code)
            print(f"{self.name} successfully enrolled in {course.name}")
        else:
            print(f"Failed to enroll{self.name} in {course.name}: Course full.")
            
    def add_classes_taken(self, course):
       self.finished_courses.append(course)
       print(f"{self.name} has completed {course.code}.")
       
    def get_enrolled_courses(self):
        return self.enrolled_courses
       
    def drop_class(self, course_code):
        print(self.enrolled_courses)
        print(course_code.code)
        if course_code.code in self.enrolled_courses:
            self.enrolled_courses.remove(course_code.code)
            print(f"{self.name} has dropped {course_code}.")
            for self.name in course_code.enrolled_students:
                course_code.enrolled_students.remove(self.name)
                print(f"{self.name} has been removed from the enrolled students of {course_code}.")
                        
       
# creating an object of the Student class
emma = Student("Emma", "NU1")

# create courses
ENGW1110 = Course("First Year Writing","ENGW1110", 45)
ENGW1111 = Course("Introductory First Year Writing", "ENGW1111", 40)
ENGW3315 = Course("Interdisciplinary Advanced Writing", "ENGW3315", 40)
EECE2140 = Course("Fundamentals of Computing for Engineers", "EECE2140", 35)

# add prerequisites
ENGW3315.add_prerequisites(ENGW1110)
ENGW3315.add_prerequisites(ENGW1111)

# print prerequisites
print("The prerequisites for this course are:")
print(ENGW3315.get_prerequisites())
print(" ")

# add classes Emma took
emma.add_classes_taken(ENGW1110)
print(" ")

# enroll Emma into class
emma.enroll(ENGW3315)
print(" ")
emma.enroll(EECE2140)
print(" ")

# print enrolled classes
print("These are the classes the student is currently enrolled in:")
emma_enrolled = emma.get_enrolled_courses()
print(emma_enrolled)
print(" ")

# print students in the class EECE2140
print(EECE2140.get_enrolled_students())

drop = input("Do you want to drop a class? Type y for yes and anything else for no. ")
if drop.lower() == 'y':
    drop_course_code = eval(input("Enter the course code you want to drop: "))
    if drop_course_code.code in emma_enrolled:
        emma.drop_class(drop_course_code)
        print(f"The student is only in these classes now: {emma_enrolled}")
    else:
        print(f"Student not enrolled in {drop_course_code}. Cannot be dropped.")

# print students in the class EECE2140
print(EECE2140.get_enrolled_students())
    