import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import math


path = "D:\Freq\list2"

lamdaby2 = []
lambda3by4 = []
lambdaby4 = []
lambdaby8 = []

for file in os.listdir(path):
    file1 = open(os.path.join(path,file),"rb")
    array = pickle.load(file1)
    lamdaby2.append(array[0])
    lambda3by4.append(array[1])
    lambdaby4.append(array[2])
    lambdaby8.append(array[3])


x_axis = [1,2,3,4,5,6,7,8]

plt.plot(x_axis,lamdaby2,label = "lamda/2")
plt.plot(x_axis[0],lamdaby2[0],'ro')
plt.plot(x_axis[1],lamdaby2[1],'ro')
plt.plot(x_axis[2],lamdaby2[2],'ro')
plt.plot(x_axis[3],lamdaby2[3],'ro')
plt.plot(x_axis[4],lamdaby2[4],'ro')
plt.plot(x_axis[5],lamdaby2[5],'ro')
plt.plot(x_axis[6],lamdaby2[6],'ro')
plt.plot(x_axis[7],lamdaby2[7],'ro')
plt.plot(x_axis,lambda3by4,label = "3lamda/4")
plt.plot(x_axis[0],lambda3by4[0],'go')
plt.plot(x_axis[1],lambda3by4[1],'go')
plt.plot(x_axis[2],lambda3by4[2],'go')
plt.plot(x_axis[3],lambda3by4[3],'go')
plt.plot(x_axis[4],lambda3by4[4],'go')
plt.plot(x_axis[5],lambda3by4[5],'go')
plt.plot(x_axis[6],lambda3by4[6],'go')
plt.plot(x_axis[7],lambda3by4[7],'go')
plt.plot(x_axis,lambdaby4,label = "lamda/4")
plt.plot(x_axis[0],lambdaby4[0],'yo')
plt.plot(x_axis[1],lambdaby4[1],'yo')
plt.plot(x_axis[2],lambdaby4[2],'yo')
plt.plot(x_axis[3],lambdaby4[3],'yo')
plt.plot(x_axis[4],lambdaby4[4],'yo')
plt.plot(x_axis[5],lambdaby4[5],'yo')
plt.plot(x_axis[6],lambdaby4[6],'yo')
plt.plot(x_axis[7],lambdaby4[7],'yo')
plt.plot(x_axis,lambdaby8,label = "lamda/8")
plt.plot(x_axis[0],lambdaby8[0],'ko')
plt.plot(x_axis[1],lambdaby8[1],'ko')
plt.plot(x_axis[2],lambdaby8[2],'ko')
plt.plot(x_axis[3],lambdaby8[3],'ko')
plt.plot(x_axis[4],lambdaby8[4],'ko')
plt.plot(x_axis[5],lambdaby8[5],'ko')
plt.plot(x_axis[6],lambdaby8[6],'ko')
plt.plot(x_axis[7],lambdaby8[7],'ko')

plt.legend()
plt.show()

