import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import math

import serial


path = "D:\Freq\list2"
store_path = "D:\Freq2"

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




filepath_dll = "E:\dnNIDLL"
file_exe = "LCVRRESPONSE.exe"
store_path = "D:\Freq2"

from serial_connection import *
import esp2 as esp
esp.initialise(1)
rot = input("enter the esp angle")
esp.move(1,float(rot))

#================================ initialise the esp ==========================

start_time = time.time()
while (time.time() - start_time < 2):
    loop = 1
#================================  initialise the serial com ===================
try:
    ComPort = serial.Serial('COM9')  # open COM9
except:
    print("failed to open the port")
ComPort.baudrate = 9600 # set Baud rate to 9600
ComPort.bytesize = 8    # Number of data bits = 8
ComPort.parity   = 'N'  # No parity
ComPort.stopbits = 1    # Number of Stop bits = 1
#==============================================================================

start_f = 1
end_f = 8
counter=0


start = input("start")

while start_f <= end_f:
    #epoch = input("start another epoch??")
    epoch = "y"
    if epoch == "y":
        data2 = str("f").encode()
        No = ComPort.write(data2)
        rec = ComPort.read()
        if rec.decode() == "f":  ## SEND THE SPECIFIED FREQUENCY
            freq_value = start_f#input("enter frequency value")
            ret_val = freq_to_string(freq_value)
            for a in range(len(ret_val)):
                print(ret_val[a])
                data2 = str(ret_val[a]).encode()
                No = ComPort.write(data2)
        start_f += 1
        print(start_f)

        #yes = input("loop for voltage")
        #if yes == "y":
        #    data2 = str("v").encode()
        #    No = ComPort.write(data2)
        #    rec = ComPort.read()

        start_time = time.time()
        while (time.time() - start_time < 1):
            loop = 1
        start = "y"#input("start aquiring data??")
        if start == "y":
            i=1
            while i:
                i-=1
                voltage_to_string(voltage_to_hex(lamdaby2[counter]+adjust))
                os.startfile(os.path.join(filepath_dll, file_exe))              #p = subprocess.Popen(os.path.join(filepath, file))  # os.startfile(os.path.join(filepath, file))
                start_time = time.time()
                print(lambdaby4[counter])
                while (time.time() - start_time < 1.5):
                    loop = 1
                data2 = str("v").encode()
                No = ComPort.write(data2)
                rec = ComPort.read()
                start_time = time.time()
                while (time.time() - start_time < 0.2):
                    loop = 1
                for a in range(len(volt_string)):
                    #print(volt_string[a])
                    data2 = str(volt_string[a]).encode()
                    No = ComPort.write(data2)
                # ========================================WAIT FOR THE PROCESS TO COMPLETE==================
                start_time = time.time()
                while (time.time() - start_time < 3):
                    loop = 1
                # =========================================PROCESS IS COMPLETED==============================
                f = open("DataNIAD_temp.txt")
                name = "DataNIAD_THETA=" + str(theta) + "freq=" + str(freq_value) + "KHZ_"  + "volts" + ".txt"
                f1 = open(os.path.join(store_path, name), "w")
                for x in f.readlines():
                    f1.write(x)
                f.close()
                f1.close()
                counter+=1
#=======================================================================================================================
#                                           set the voltage to zero again
#=======================================================================================================================
                #delay  = input("dalay")
                start_time = time.time()
                while (time.time() - start_time < 2):
                    loop = 1
                voltage_to_string(voltage_to_hex(0))
                print("0")
                data2 = str("v").encode()
                No = ComPort.write(data2)
                rec = ComPort.read()
                start_time = time.time()
                while (time.time() - start_time < 0.2):
                    loop = 1
                for a in range(len(volt_string)):
                    # print(volt_string[a])
                    data2 = str(volt_string[a]).encode()
                    No = ComPort.write(data2)
                # ========================================WAIT FOR THE PROCESS TO COMPLETE==================
                start_time = time.time()
                while (time.time() - start_time < 1):
                    loop = 1





