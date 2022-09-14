import csv
import re
import pandas

def urlHausOpen(filename):
    file = pandas.read_csv(filename, skiprows=9)
    
    for row in file:
        while row <= 9:
            pass
        else:
        #row.split(",")
            print(row)