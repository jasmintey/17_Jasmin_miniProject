import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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

grp1date = grp1['Period'].str.split(' ', n = 1, expand = True)
print(grp1date)

grp1 = grp1.assign(grp1date_year=grp1date[1])
print(grp1)

grp1.index = grp1['grp1date_year']
print(grp1.index)

ps = grp1['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('year', fontsize=5)
plt.ylabel('No. of calories', fontsize=10)
plt.xticks(index, ps.index, fontsize=10)
plt.title('[1900-1910]')
plt.bar(ps.index, ps.values)
plt.show()

