"""
------------------------------------------------------------------------
Lab 2, Task 1
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-09-15"
------------------------------------------------------------------------
"""
celsius = 0
fahrenheit = 0
FAHRENHEIT_FREEZING = 32
celsius_to_fahrenheit_conversion = 9/5
celsius = int(input("Temperature (C):"))
fahrenheit = celsius_to_fahrenheit_conversion * \
    celsius + FAHRENHEIT_FREEZING
print("Temperature (F):", fahrenheit)
