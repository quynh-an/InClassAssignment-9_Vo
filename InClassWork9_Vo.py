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
            for course in self.prereqs:
                if course in student.finished_courses:
                    self.enrolled_students.append(student)
            return True
        else:
            return False
        
    def is_full(self):
        return len(self.enrolled_students) >= self.max_students
    
    def add_prerequisites(self, prereq_course_code):
        self.prereqs.append(prereq_course_code.code)
        
    def get_prerequisites(self):
        return self.prereqs

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []
        self.finished_courses = []
    
    def enroll(self, course):
        if course.add_student(self):
            self.enrolled_courses.append(course)
            print(f"{self.name} successfully enrolled in {course.name}")
        else:
            print(f"Failed to enroll{self.name} in {course.name}: Course full.")
            
    def add_classes_taken(self, course):
       self.finished_courses.append(course)
       print(f"{self.name} has completed {course.code}.")
       
# creating an object of the Student class
emma = Student("Emma", "NU1")

# create courses
ENGW1110 = Course("First Year Writing","ENGW1110", 45)
ENGW1111 = Course("Introductory First Year Writing", "ENGW1111", 40)
ENGW3315 = Course("Interdisciplinary Advanced Writing", "ENGW3315", 40)

# add prerequisites
ENGW3315.add_prerequisites(ENGW1110)
ENGW3315.add_prerequisites(ENGW1111)

# print prerequisites
print("The prerequisites for this course are:")
print(ENGW3315.get_prerequisites())

# add classes Emma took
emma.add_classes_taken(ENGW1110)

# enroll Emma into class
emma.enroll(ENGW3315)


