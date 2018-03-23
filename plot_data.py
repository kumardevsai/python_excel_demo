#!/usr/bin/env python
import xlrd
import datetime
import time
import matplotlib.pyplot as plt

wb = xlrd.open_workbook('data.xls')

datemode = wb.datemode
sh = wb.sheet_by_index(0)

columns = []

# First column: dates
col_values = sh.col_values(0)
col_values = col_values[1:len(col_values)] # omit first row
column = [datetime.datetime(*xlrd.xldate_as_tuple(date, datemode)) for date in col_values]
columns.append(column)

for column in range(1,6):
    col_values = sh.col_values(column)
    col_values = col_values[1:len(col_values)] # omit first row
    
    column = [time * 24 for time in col_values]
    columns.append(column)

days = columns[0]

DAY_CHANGE = 5 # at 2:00 the next day beginns
for i in range(len(columns[1])):
    if columns[1][i] < DAY_CHANGE:
        columns[1][i] += 24

fig = plt.figure()

ax = fig.add_subplot(111)
plt.plot(days, columns[1], 'b--', 
     days, columns[2], 'g:', 
     days, columns[3], 'b.',
     days, columns[4], 'g-',
     days, columns[5], 'b-')

leg = ax.legend(('T1', 'T2', 'L1', 'D', 'L2'),
           'upper center')

plt.show()





