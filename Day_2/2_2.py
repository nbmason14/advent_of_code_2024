import csv

#TODO

reports = {'Safe':0,'Unsafe':0}

with open("C:/Users/masonnea/Github/advent_of_code_2024/Day_2/input_Day2.csv","r") as file:
    reader = csv.reader(file, delimiter=" ")
    for i,line in enumerate(reader):
        Unsafe = 0
        inc = 0
        dec = 0
        for j in range(0,len(line)-1):
            if abs(int(line[j+1])-int(line[j])) <1 or abs(int(line[j+1])-int(line[j])) > 3:
                reports['Unsafe'] = reports.get('Unsafe')+1
                Unsafe = 1
                break
            if int(line[j]) > int(line[j+1]):
                inc += 1
            else:
                dec += 1
        if Unsafe == 0 and (inc == 0 or dec == 0):
            reports['Safe'] = reports.get('Safe')+1

print(reports['Safe'])



