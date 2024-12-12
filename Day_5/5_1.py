import os
import re


os.chdir("H:/GitHub/advent_of_code_2024/Day_5/")

f = open("H:/GitHub/advent_of_code_2024/Day_5/input.txt","r")
text = f.readlines()

rules = {}
correct = []
i=0
while text[i] != "\n":
    items = re.findall(r"[0-9]{1,2}",text[i])
    if items[0] not in rules:
        rules[items[0]] = {items[1]}
    else:
        rules[items[0]].add(items[1])
    
    i+=1

i+=1
count = 0
sum = 0
while i < len(text):
    lis = text[i].split(",")
    correct = True
    for j in range(0,len(lis)):
        if lis[j] in rules:
            for k in range(j,-1,-1):
                if lis[k] in rules[lis[j]]:
                    correct = False
    if correct:
        count +=1
        l = len(lis)
        if l%2 == 0:
            sum += int(lis[int(l/2)])
        elif l%2 == 1:
            sum += int(lis[int((l-1)/2)])
    i += 1
    print(i)
print(count)
print(sum)