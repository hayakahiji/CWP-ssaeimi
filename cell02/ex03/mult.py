#!/usr/bin/env python3

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

multiply = first_number * second_number

if multiply < 0:
    print(f"{first_number} x {second_number} = {multiply}")
    print("This result is negative.") 
elif multiply > 0:
    print(f"{first_number} x {second_number} = {multiply}")
    print("This result is positive.") 
else:
    print(f"{first_number} x {second_number} = {multiply}")
    print("This result is positive and negative.")  