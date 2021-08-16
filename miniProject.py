import matplotlib.pyplot as plt # import matplotlib so that the data can work
import pandas as pd
import numpy as np
file = pd.read_excel('dataNew.xls') # import the dataNew.xls : file
print(file) # Print out file

date = file['Period'].str.split(' ', n = 1, expand = True) # Create another dataframe by spilting the Period.
print(date)

file = file.assign(date_year=date[1]) # assign a new column named date_year
print(file)

file.index = file['date_year'] # Print original indexes
print(file.index)

grp1 = file.iloc[:11] # Summarize the first 11 columns
print(grp1)
grp2 = file.iloc[11:21] # Summarize the first 11 columns to 21 columns
print(grp2)
grp3 = file.iloc[21:] # Summarize the last 21 columns
print(grp3)


grp1sum = sum(grp1['Calories'])
print(round(grp1sum, 1))
grp2sum = sum(grp2['Calories'])
print(grp2sum)
grp3sum = sum(grp3['Calories'])
print(grp3sum)

grp1mean = grp1sum / len(grp1['Calories']) # Find the mean for the dataframe columns
print(round(grp1mean, 2))
grp2mean = grp2sum / len(grp2['Calories'])
print(round(grp2mean, 2))
grp3mean = grp3sum / len(grp3['Calories'])
print(round(grp3mean, 2))

ps = grp1['Calories'].sort_values() # find the calories in the data file and present the result in bar chart in ascending order
plt.xlabel('Year', fontsize=10)
plt.ylabel('No. of calories', fontsize=10)
plt.title('1900-1910')
plt.bar(ps.index, ps.values)
plt.show()

ps = grp2['Calories'].sort_values()
plt.xlabel('Year', fontsize=10)
plt.ylabel('No. of calories', fontsize=10)
plt.title('1911-1920')
plt.bar(ps.index, ps.values)
plt.show()

ps = grp3['Calories'].sort_values()
plt.xlabel('Year', fontsize=10)
plt.ylabel('No. of calories', fontsize=10)
plt.title('1921-1930')
plt.bar(ps.index, ps.values)
plt.show()

class EvaluateMarks:
    def totalgrp1(num):
        return sum(num)

    def meangrp1(num):
        return sum(num)/ len(num)

    def totalgrp2(num):
        return sum(num)

    def meangrp2(num):
        return sum(num)/ len(num)

    def totalgrp3(num):
        return sum(num)

    def meangrp3(num):
        return sum(num)/ len(num)

print(round(EvaluateMarks.totalgrp1(grp1['Calories']), 1))
print(round(EvaluateMarks.totalgrp2(grp2['Calories']), 1))
print(round(EvaluateMarks.totalgrp3(grp3['Calories']), 1))

print(round(EvaluateMarks.meangrp1(grp1['Calories']), 1))
print(round(EvaluateMarks.meangrp2(grp2['Calories']), 1))
print(round(EvaluateMarks.meangrp3(grp3['Calories']), 1))
