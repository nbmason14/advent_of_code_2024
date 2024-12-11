import re
import os
os.chdir("H:/GitHub/advent_of_code_2024/Day_3/")

f = open("H:/GitHub/advent_of_code_2024/Day_3/input.txt","r")
text = f.read()
matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)",text)
#print(matches)

sum = 0
for i in matches:
    items = re.findall(r"[0-9]{1,3}",i)
    sum += (int(items[0]) * int(items[1]))

print(sum)