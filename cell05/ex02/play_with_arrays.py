#!/usr/bin/env python3
ori_arr = [2,8,9,48,8,22,-12,2]
new_arr = []

print(f"Original array: {ori_arr}")


i = 0

while i < len(ori_arr):
    
    ori_arr[i] += 2
    if ori_arr[i] > 5:
        new_arr.append(ori_arr[i])
    i+=1



print(f"New array: {new_arr}")