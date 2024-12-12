import re
import os

os.chdir("H:/GitHub/advent_of_code_2024/Day_4/")

f = open("H:/GitHub/advent_of_code_2024/Day_4/input.txt","r")
text = f.readlines()

count = 0
for i in range(140):
    matches_front = re.findall(r"XMAS",text[i])
    matches_back = re.findall(r"SAMX",text[i])
    count += len(matches_front)
    count += len(matches_back)
    for j in range(140):
        if text[i][j] == "X" and i <= 136 and j <= 136:
            if text[i+1][j+1] == "M" and text[i+2][j+2] == "A" and text[i+3][j+3] == "S":
                count += 1
        if text [i][j] == "X" and i <= 136:
            if text[i+1][j] == "M" and text[i+2][j] == "A" and text[i+3][j]  == "S":
                count += 1
        if text[i][j] == "X" and j >= 3 and i <= 136:
            if text[i+1][j-1] == "M" and text[i+2][j-2] == "A" and text[i+3][j-3]  == "S":
                count += 1
        if text[i][j] == "X" and i >= 3:
            if text[i-1][j] == "M" and text[i-2][j] == "A" and text[i-3][j] == "S":
                count += 1
        if text[i][j] == "X" and i >= 3 and j <= 136:
            if text[i-1][j+1] == "M" and text[i-2][j+2] == "A" and text[i-3][j+3] == "S":
                count += 1
        if text[i][j] == "X" and i >= 3 and j >= 3:
            if text[i-1][j-1] == "M" and text[i-2][j-2] == "A" and text[i-3][j-3] == "S":
                count += 1
print(count)



