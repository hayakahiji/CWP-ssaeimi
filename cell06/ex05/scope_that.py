#!/usr/bin/env python3

def add_one(x):
    return x+1

num = 4

print(f"Before: {num}")

add_one(num)

print(f"After: {num}")

""" เนื่องจากในฟังก์ชัน return ค่ากลับมา แปลว่าต้องมีตัวแปรสักหนึ่งตัวมารองรับ ถ้าไม่มีก็ควรใช้ print(add_one(num)) ไม่อย่างนั้นจะไม่เกิดการอัพเดตค่าขึ้น"""