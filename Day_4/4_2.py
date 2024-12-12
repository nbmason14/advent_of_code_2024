import re
import os

os.chdir("H:/GitHub/advent_of_code_2024/Day_4/")

f = open("H:/GitHub/advent_of_code_2024/Day_4/input.txt","r")
text = f.readlines()

count_1 = 0
valid_strings = {'MS','SM'}
for i in range(140):
    for j in range(140):
        count_2 = 0
        if text[i][j] == "A" and i >= 1 and j >= 1 and i <= 138 and j <= 138:
            if text[i-1][j-1] + text[i+1][j+1] in valid_strings:
                count_2 += 1
            if text[i-1][j+1] + text[i+1][j-1] in valid_strings:
                count_2 += 1
        if count_2 == 2:
            count_1 += 1

print(count_1)



