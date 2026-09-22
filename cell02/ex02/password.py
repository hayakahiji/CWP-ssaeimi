#!/usr/bin/env python3
import sys

password = "Python is awesome"

user = sys.argv[1]

if user == password:
    print("ACESS GRANTED")
elif user != password:
    print("ACESS DENIED")

