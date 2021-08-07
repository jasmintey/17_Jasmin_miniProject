import pandas as pd
file = pd.read_excel('dataNew.xls')
print(file)

grp1 = file.iloc[:11]
print(grp1)
grp2 = file.iloc[11:21]
print(grp2)
grp3 = file.iloc[21:]
print(grp3)

print(sum(grp1['Calories']))
hi jassssssssss