import math

print(math.sqrt(3))
print(math.pi)
print(math.floor(2.9))
print(math.ceil(2.6))
print(math.pow(2,6))
print(math.log10(10000))
import calendar

print(calendar.month(2002,3))
print(calendar.isleap(2000))
print(dir(calendar))
import sys
sys.path.append("F:\Study\Assembly")
import function as f
pat=f.print_pattern(10)
print(pat)

std={}

std['c_Dep']={
    'Name': 'Ali Hassan',
    'sem': '4th',
    'r_No': '206',
}
std['p_Dep']={
    'Name': 'Ali Hassan',
    'sem': '4th',
    'r_No': '219',
}

import json
s=json.dumps(std)
with open("F://Study//Data Science//dic.txt","w") as f:
    f.write(s)
import area
print("Iam in modules .py")
