#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    found = False
    ans = ""
    for ch in s:
        if ch == "z":
            ans += "z"
            found = True
    if not found:
        print("none")
    print(ans)