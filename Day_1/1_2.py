import pandas as pd

file = pd.read_csv("C:/Users/masonnea/Github/advent_of_code_2024/Day_1/1_1_input.csv",delimiter=",",header=None,index_col=False,names=["0","1"])

col1 = file.loc[:,'0']
col2 = file.loc[:,'1']
col2_dict = {}
total = 0

for i in range(0,len(col2)):
    if col2[i] in col2_dict:
        col2_dict[col2[i]] = col2_dict.get(col2[i]) + 1
    else:
        col2_dict[col2[i]] = 1

for i in range(0,len(col1)):
    if col1[i] in col2_dict:
        total += (col1[i] * col2_dict.get(col1[i]))

print(total)