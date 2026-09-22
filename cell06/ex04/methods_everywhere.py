#!/usr/bin/env python3
import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    """ ถ้า string ที่รับเข้ามามีอักษรไม่ถึง 8 ตัว ให้เพิ่ม Z เข้าไปให้ครบ"""
    print(s + ("Z" * (8 - len(s))))

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)