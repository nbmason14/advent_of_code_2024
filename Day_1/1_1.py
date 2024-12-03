import pandas as pd

file = pd.read_csv("advent_of_code_2024/Day_1/1_1_input.csv",delimiter=",",header=None,index_col=False,names=["0","1"])

col1 = file.loc[:,'0']
col1 = col1.sort_values()
col2 = file.loc[:,'1']
col2 = col2.sort_values()
total = 0


for i in range(0,min(len(col1),len(col2))):
    total += abs(col1.values[i]-col2.values[i])
    
print(total)