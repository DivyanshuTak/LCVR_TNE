import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import math

import serial



file = open(os.path.join("D:\Freq\list","8I_0"),"rb")
I_02 = pickle.load(file)
file.close()

file1 = open(os.path.join("D:\Freq\list","8I_90"),"rb")
I_902 = pickle.load(file1)
file1.close()

number=8


file2 = open("volt2","rb")
volt2 = pickle.load(file2)
file2.close()


voltage_vals = volt2[:len(volt2)-16]

#print(voltage_vals)
#while True:
#    pass


list = []                               # order lamda/2,3lamda/4,lamda/4,lamda/8

retardence = []
list_of_retardence = []
list_of_volts = []



filepath_dll = "E:\dnNIDLL"
file_exe = "LCVRRESPONSE.exe"


def interpolate(y_val,x,y):
    for a in range(len(y)):
        if (abs(y[a] - y_val) < abs(y[a] - y[a+1])) and (abs(y[a+1] - y_val) < abs(y[a] - y[a+1])):#val>y[a] and y<y[a+1]:
            deltay = abs(y[a+1] - y[a])
            deltax = abs(x[a+1] - x[a])
            deltaydash = abs(y_val - y[a])
            ratio = deltaydash/deltay
            x_val = x[a] + ratio*deltax
            return x_val


for itr in range(len(I_02)):
    core = ((I_02[itr] - I_902[itr])/(I_02[itr] + I_902[itr]))
    val = math.acos(core)
    degree = val*(180/math.pi)
    #if degree > 125 :
    #    diff = degree - 125
    #    degree -= diff
    #degree /= 360
    retardence.append(degree)

'''
x_val = interpolate(90,volt,retardence)


xs = np.sort(volt)
ys = np.array(retardence)[np.argsort(volt)]

# x coordinate
x0 = x_val
# interpolated y coordinate
y0 = np.interp(x0, xs, ys)

print(x_val,y0)
'''

index = np.where(retardence == np.max(retardence))
diff_max = np.max(retardence) - retardence[0]
center = 90 + retardence[1]
a=0
while a<int(index[0]):
    diff = center - retardence[a]
    retardence[a] = 360 - retardence[a]
    a+=1



#plt.plot(volt2,I_02)
plt.plot(voltage_vals,retardence)
plt.show()



for a in range(4):
    val = input("enter the fraction of lameda")
    val_degree = float(val)*360
    list_of_volts.append(interpolate(val_degree,voltage_vals,retardence))

file2 = open(os.path.join("D:\Freq\list2" , str(number)),"wb")
pickle.dump(list_of_volts,file2)
file2.close()


while True:
    pass

from serial_connection import *
import esp2 as esp
esp.initialise(1)
rot = input("enter the esp angle")
esp.move(1,float(rot))


#========================================================================================
#                                           START THE LOOPING FOR VOLT VALUES HERE
#========================================================================================





for a in range(4):
    val = input("enter the fraction of lameda")
    val_degree = float(val)*360
    list_of_volts.append(interpolate(val_degree,volt2,retardence))


destination_path = "E:\detector_transient_response"
'''

                            START THE SERIAL CONNECTION AND VOLTAGE CONTROL
                            ESP IS SET AT 90 DEGREE AS IT GIVES MAX. INTENSITY
'''
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


while True:
    epoch = input("start another epoch??")
    if epoch == "y":
        data2 = str("f").encode()
        No = ComPort.write(data2)
        rec = ComPort.read()
        if rec.decode() == "f":  ## SEND THE SPECIFIED FREQUENCY
            freq_value = input("enter frequency value")
            ret_val = freq_to_string(freq_value)
            for a in range(len(ret_val)):
                print(ret_val[a])
                data2 = str(ret_val[a]).encode()
                No = ComPort.write(data2)
        itr = 0
        #yes = input("loop for voltage")
        #if yes == "y":
        #    data2 = str("v").encode()
        #    No = ComPort.write(data2)
        #    rec = ComPort.read()

        start = input("start aquiring data??")
        if start == "y":
            while itr < len(list_of_volts):
                voltage_to_string(voltage_to_hex(list_of_volts[itr]+adjust))
                os.startfile(os.path.join(filepath_dll, file_exe))              #p = subprocess.Popen(os.path.join(filepath, file))  # os.startfile(os.path.join(filepath, file))
                start_time = time.time()
                print(list_of_volts[itr])
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
                name = "DataNIAD_THETA="+ str(theta)+"freq=" + str(freq_value) + "KHZ_" + str(list_of_volts[itr]) + "volts" + ".txt"
                f1 = open(os.path.join(destination_path,name), "w")
                for x in f.readlines():
                    f1.write(x)
                f.close()
                f1.close()
#=======================================================================================================================
#                                           set the voltage to zero again
#=======================================================================================================================
                delay  = input("dalay")
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
                itr+=1


























