import numpy as np
import matplotlib.pyplot as plt
import os
import pickle

path_0 = "D:\Freq\One\zero"#"D:\Freq\One\zero"#"E:\data_aq\zero"
path_90 = "D:\Freq\One\otho"#"D:\Freq\One\otho"#"D:\data\otho"   # E:\data_aq\orthogonal"
number = 1
voltage = []
time  = []
detector_output = []
output = []
inputvolt = []
I_03 = []
I_903 = []

def shift(l, n):
     return l[n:] + l[:n]

'''
for file in os.listdir(path_0):
    detector_output = []
    with open(os.path.join(path_0,file)) as infile:
        #print(file)
        for line in infile:
            val = float(line.split()[3])
            detector_output.append((val))

        #temparr = voltage[int(len(voltage)/2):len(voltage)]
        #print(len(temparr)*np.mean(temparr))
        itr = 60000#int(len(voltage) / 2)
        offset = 0
        count=1
        while itr <= 80000:
            offset = abs(offset) + abs(detector_output[itr])
            itr += 1
            count+=1
        volt = float(file[27:32])
        inputvolt.append(volt)
        I_03.append(offset/count)
        #print(volt)
    #val = input("val")

#name_0 = "D:\Freq\list" + "4" + "I_0"
file1 = open(os.path.join("D:\Freq\list" , str(number) + "I_0"),"wb")
pickle.dump(I_03,file1)
file1.close()


#name_volt = "D:\Freq\list" + "4" + "volt"
file3 = open(os.path.join("D:\Freq\list" , str(number) + "volt"),"wb")
pickle.dump(inputvolt,file3)
file3.close()


'''
''' 
             #   so far here the voltage list and i1 list is made
             #   for next iteration only i2 is required
'''

'''
for file in os.listdir(path_90):
    detector_output = []
    with open(os.path.join(path_90,file)) as infile:
        for line in infile:
            val = float(line.split()[3])
            detector_output.append((val))

        #temparr = voltage[int(len(voltage)/2):len(voltage)]
        #print(len(temparr)*np.mean(temparr))
        itr = 70000#int(len(voltage) / 2)
        offset = 0
        count=1
        while itr <= 80000:
            offset = abs(offset) + abs(detector_output[itr])
            itr += 1
            count+=1
        #volt = float(file[27:32])
        #inputvolt.append(volt)
        I_903.append(offset/count)


#name_90 = os.path.join("D:\Freq\list" , "4" + "I_90")
file2 = open(os.path.join("D:\Freq\list" , str(number) + "I_90"),"wb")
pickle.dump(I_903,file2)
file2.close()


#file3 = open("volt4","wb")
#pickle.dump(inputvolt,file3)
#file3.close()


print("done")



'''



path_with = "E:\detector_transient_response\wtransient_128"#"D:\Freq2\With"#"E:\detector_transient_response\wtransient_128"
path_without = "E:\detector_transient_response\without_transient2" #"D:\Freq2\Without"#"E:\detector_transient_response\without_transient2"
path_dark = "E:\detector_transient_response\dark_offset"


start_time=0
end_time=0
time_diff = []
time_diffw = []
start = itr = 10000
end = 30000
end_val = []
end_valw = []
counter=0
for file in os.listdir(path_with):
    voltage=[]
    time=[]
    detector_output = []
    voltagew = []
    timew = []
    dark = []
    time_dark = []
    detector_outputw = []
    with open(os.path.join(path_with,file)) as infile:
        for line in infile:
            val = float(line.split()[2])
            voltage.append((val))
            time.append(float(line.split()[1]))
            detector_output.append(float(line.split()[3]))

    with open(os.path.join(path_without,file)) as infile2:
        for line2 in infile2:
            val2 = float(line2.split()[2])
            voltagew.append((val2))
            timew.append(float(line2.split()[1]))
            detector_outputw.append(float(line2.split()[3]))

    #with open(os.path.join(path_dark,file)) as infile2:
    #    for line2 in infile2:
    #        dark.append(float(line2.split()[3]))
    #        time_dark.append(float(line2.split()[1]))

    #detector_output = np.subtract(detector_output,dark)
    temp = detector_output[60000:70000]
    end_val.append(np.mean(temp))
    #print(end_val)
    #detector_outputw = np.subtract(detector_outputw, dark)
    temp = detector_outputw[60000:70000]
    end_valw.append(np.mean(temp))
    #print(end_valw)
    #for c in range(len(dark)):
    #    detector_outputw[c] = detector_outputw[c] - dark[c]
    #    detector_output[c] = detector_output[c] - dark[c]



    #plt.plot(timew[20000:30000],voltagew[20000:30000])
    #plt.plot(timew[20000:30000], detector_outputw[20000:30000])
    #plt.show()

    mean=0
    itr = start
    diff=0
    while diff < 2:
        diff = abs(voltage[itr+1] - voltage[itr])
        itr+=1
    start_time = time[itr]
    temp1 = itr
    while not ((abs(mean)>abs(end_val[counter])-0.005)and(abs(mean)<abs(end_val[counter])+0.005)):
        mean = np.mean(detector_output[itr-200:itr + 1000])
        #mean = np.mean(
        #    [detector_output[itr + 1], detector_output[itr + 2], detector_output[itr + 3], detector_output[itr + 4],
        #     detector_output[itr + 5], detector_output[itr + 6]])
        itr += 1
    end_time = time[itr]
    time_diff.append(end_time-start_time)
    #print(temp1)
    #print(itr)
    #print(time_diff)
    #plt.plot(time[10000:40000],detector_output[10000:40000])
    #plt.plot(time[temp1],detector_output[temp1],'ro')
    #plt.plot(time[itr],detector_output[itr],'ro')
    #plt.show()
    itr2=start
    mean=0
    diff=0
    while diff < 0.6:
        diff = abs(voltagew[itr2+1] - voltagew[itr2])
        itr2+=1
    start_time2 = timew[itr2]
    temp = itr2
    while not ((abs(mean)>abs(end_valw[counter])-0.005)and(abs(mean)<abs(end_valw[counter])+0.005)):
        mean = np.mean(detector_outputw[itr2-200:itr2+1000])
        #mean = np.mean(
        #    [detector_outputw[itr2 + 1], detector_outputw[itr2 + 2], detector_outputw[itr2 + 3], detector_outputw[itr2+ 4],
        #     detector_outputw[itr2 + 5], detector_outputw[itr2 + 6]])
        itr2 += 1
    end_time2 = timew[itr2]
    time_diffw.append(end_time2-start_time2)
    #print(temp)
    #print(itr2)
    #print(time_diffw)
    #plt.plot(timew[10000:40000], detector_outputw[10000:40000])
    #plt.plot(timew[temp], detector_outputw[temp], 'ro')
    #plt.plot(timew[itr2], detector_outputw[itr2], 'ro')
    #plt.show()

    plt.subplot(2, 1, 1)
    plt.xticks([]), plt.yticks([])
    plt.title("with transient")
    plt.plot(time[20000:30000], detector_output[20000:30000])
    plt.plot(time[itr], detector_output[itr], 'ro')
    plt.plot(time[temp1], detector_output[temp1], 'ro')
    plt.subplot(2, 1, 2)
    plt.xticks([]), plt.yticks([])
    plt.title("without transient")
    plt.plot(timew[20000:30000], detector_outputw[20000:30000])
    plt.plot(timew[itr2], detector_outputw[itr2], 'ro')
    plt.plot(timew[temp], detector_outputw[temp], 'ro')
    plt.show()



    counter += 1



    #plt.plot(timew[20000:30000], detector_outputw[20000:30000])
    #plt.plot(timew[itr2],detector_outputw[itr2],'ro')
    #plt.plot(timew[temp], detector_outputw[temp], 'ro')
    #plt.show()
    #itr=start
    #while itr < end:
    #    diff = abs(detector_output[itr] - detector_output[itr+1])
        #diffw = abs(detector_outputw[itr] - detector_outputw[itr + 1])
    #    itr2 = itr
    #    if diff > 0.5:
    #        mean = 0
    #        start_time = time[itr]
    #        while not ((abs(mean)>abs(end_val[counter])-0.005)and(abs(mean)<abs(end_val[counter])+0.005)):
    #            mean = np.mean([detector_output[itr2+1],detector_output[itr2+2],detector_output[itr2+3],detector_output[itr2+4],detector_output[itr2+5],detector_output[itr2+6]])
    #            itr2+=1
    #            end_time = time[itr2]
    #        time_diff.append((end_time-start_time))
    #        itr=end
    #    itr+=1

    #print((detector_output[int(start_time)] - detector_outputw[start_time]))



    #itr = start
    #while itr < end:
       #diff = abs(detector_output[itr] - detector_output[itr + 1])
    #    diffw = abs(detector_outputw[itr] - detector_outputw[itr + 20])
    #    itr2 = itr
    #    if diffw > 0.5:
    #        mean = 0
    #        start_time = timew[itr2]
    #        while not((abs(mean)>abs(end_valw
    #                             [counter])-0.005)and(abs(mean)<abs(end_valw[counter])+0.005)):
    #            mean = np.mean([detector_outputw[itr2 + 1], detector_outputw[itr2 + 2], detector_outputw[itr2 + 3],
    #                           detector_outputw[itr2 + 4], detector_outputw[itr2 + 5], detector_outputw[itr2 + 6], ])
    #            itr2 += 1
    #            end_time = timew[itr2]
    #        itr = end
    #        time_diffw.append((end_time - start_time))
    #    itr += 1
    #plt.plot(timew,detector_outputw)
    #plt.show()

    #plt.subplot(2,1,1)
    #plt.xticks([]),plt.yticks([])
    #plt.title("without transient")
    #plt.plot(timew,detector_outputw)
    #plt.plot(timew, voltagew)
    #plt.plot(time[itr], detector_outputw[itr], 'ro')
    #plt.plot(time[temp1], detector_outputw[temp1], 'ro')
    #plt.subplot(2,1,2)
    #plt.xticks([]), plt.yticks([])
    #plt.title("with transient")
    #plt.plot(timew, voltage)
    #plt.plot(timew[itr2], detector_output[itr2], 'ro')
    #plt.plot(timew[temp], detector_output[temp], 'ro')
    #plt.show()
    #plt.plot(vals, poly, markevery=mark, ls="", marker="o", label="points")






#filet = open("delta_transient","wb")
#pickle.dump(time_diff,filet)
#filet.close()

#filet = open("delta_transient","wb")
#pickle.dump(time_diff,filet)
#filet.close()

#freq_list = []
#x_axis = [1,2,3,4,5,6,7,8]
#for a in range(8):
#    freq_list.append(time_diff[a])#(time_diffw[a]-time_diff[a])


#print(freq_list)

#plt.plot(x_axis,freq_list)
#plt.plot(x_axis[0],freq_list[0],'ro')
#plt.plot(x_axis[1],freq_list[1],'ro')
#plt.plot(x_axis[2],freq_list[2],'ro')
#plt.plot(x_axis[3],freq_list[3],'ro')
#plt.plot(x_axis[4],freq_list[4],'ro')
#plt.plot(x_axis[5],freq_list[5],'ro')
#plt.plot(x_axis[6],freq_list[6],'ro')
#plt.plot(x_axis[7],freq_list[7],'ro')
#plt.show()


#print("the time difference at lamda/2 = ",(time_diffw[0]-time_diff[0]),"ms")
#print("the time difference at 3lamda/4 = ",(time_diffw[1]-time_diff[1]),"ms")
#print("the time difference at lamda/4 = ",(time_diffw[2]-time_diff[2]),"ms")
#print("the time difference at lamda/8 = ",(time_diffw[3]-time_diff[3]),"ms")




#print(time_diff)
#print(time_diffw)

'''
    if abs(detector_output[int(start_time)] - detector_outputw[int(start_time)]) < 0.08:
        count=1
        while abs(detector_output[int(start_time)] - detector_outputw[int(start_time)]) < 0.1 :
            #count+=1
            detector_outputw = shift(detector_outputw,count)
    elif abs(detector_output[int(start_time)] - detector_outputw[int(start_time)]) > 0.1:
        count = 1
        while abs(detector_output[int(start_time)] - detector_outputw[int(start_time)]) < 0.1:
            #count += 1
            detector_outputw = shift(detector_outputw, -count)

    '''


