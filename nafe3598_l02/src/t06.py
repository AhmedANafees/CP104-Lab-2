"""
------------------------------------------------------------------------
Lab 2, Task 6
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-09-15"
------------------------------------------------------------------------
"""
NUM_OF_MONTHS_IN_YEAR = 12
mortgage_principal = int(input("Mortgage principal ($): "))
num_of_years = float(input("Number of years: "))
yearly_rate = float(input("Yearly interest rate (%): "))
num_of_monthly_payments = num_of_years*NUM_OF_MONTHS_IN_YEAR
yearly_rate_percent = yearly_rate/100
monthly_rate = yearly_rate_percent/NUM_OF_MONTHS_IN_YEAR
m1 = monthly_rate*((1+monthly_rate)**num_of_monthly_payments)
m2 = ((1+monthly_rate)**num_of_monthly_payments)-1
monthly_payments = mortgage_principal*(m1/m2)
print("The monthly payments are: $", monthly_payments)
