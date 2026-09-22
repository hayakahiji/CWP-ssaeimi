#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    matches = re.findall(keyword, text) # คำใน variable keyword เทียบกับ text ว่าใน text มีคำที่ตรงกับ keyword ไหม
    if matches: # ถ้าตรงให้นับออกมาว่ามีกี่ตัว เช่น keyword = "the" , text = "the fox jums over the dog" ans 2 
        print(len(matches))
    else:
        print("none")