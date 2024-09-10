"""
------------------------------------------------------------------------
Lab 2, Task 7
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-09-15"
------------------------------------------------------------------------
"""
num_of_flyers = int(input("Number of flyers: "))
num_of_volunteers = int(input("Number of volunteers: "))
flyers_per_volunteer = num_of_flyers//num_of_volunteers
flyers_left_over = num_of_flyers % num_of_volunteers
print("Flyers per volunteer: ", flyers_per_volunteer)
print("Flyers left over: ", flyers_left_over)
