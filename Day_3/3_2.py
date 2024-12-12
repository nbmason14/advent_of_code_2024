import re
import os
os.chdir("H:/GitHub/advent_of_code_2024/Day_3/")

f = open("H:/GitHub/advent_of_code_2024/Day_3/input.txt","r")
text = f.read()
matches_do = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",text)

sum = 0
mul = True
for i in matches_do:
    if i == "do()":
        mul = True
    elif i == "don't()":
        mul = False
    else:
        if mul:
            items = re.findall(r"[0-9]{1,3}",i)
            sum += (int(items[0]) * int(items[1]))

print(sum)