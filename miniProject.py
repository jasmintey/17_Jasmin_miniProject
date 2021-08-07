import pandas as pd
file = pd.read_excel('dataNew.xls')
print(file)

grp1 = file.iloc[:11]
print(grp1)
grp2 = file.iloc[11:21]
print(grp2)
grp3 = file.iloc[21:]
print(grp3)

grp1sum = sum(grp1['Calories'])
print(round(grp1sum, 1))
grp2sum = sum(grp2['Calories'])
print(grp2sum)
grp3sum = sum(grp3['Calories'])
print(grp3sum)

grp1mean = grp1sum / len(grp1['Calories'])
print(round(grp1mean, 2))
grp2mean = grp2sum / len(grp2['Calories'])
print(round(grp2mean, 2))
grp3mean = grp3sum / len(grp3['Calories'])
print(round(grp3mean, 2))

