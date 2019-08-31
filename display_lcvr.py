import numpy as np
import os
import matplotlib.pyplot as plt
import csv
voltage = []
time = []
photodetector = []

b=np.loadtxt(r'DataNIAD.txt',dtype=str,delimiter=' ',usecols=(1,))
print(b)



'''
csv_file = r"mycsv.csv"

in_txt = csv.reader(open("DataNIAD.txt", "r"), delimiter = '\t')
out_csv = csv.writer(open("csv_file.csv", 'w'))

out_csv.writerows(in_txt)
'''
#print(voltage)



#file = open("DataNIAD.txt","r")
##print(data)