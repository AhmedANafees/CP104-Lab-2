"""
------------------------------------------------------------------------
Lab 13, Task 13
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-09-15"
------------------------------------------------------------------------
"""
MIDTERM_WEIGHT = 35
EXAM_WEIGHT = 65
midterm_mark = float(input("Midterm mark (%): "))
exam_mark = float(input("Exam mark (%): "))
final_grade = ((midterm_mark*MIDTERM_WEIGHT) + (exam_mark*EXAM_WEIGHT))/100
print("Final Grade (%): ", final_grade)
