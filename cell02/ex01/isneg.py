#!/usr/bin/env python3
import sys

number = int(sys.argv[1])

if number > 0 :
	print("This number is positive.")
elif number < 0:
	print("This number is negative.")
elif number == 0:
    print("This number is both positive and negative")
	
