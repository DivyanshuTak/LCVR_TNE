import numpy as np
import matplotlib.pyplot as plt



textfile = "DataNIAD.txt"
voltage = []
time  = []
detector_output = []

with open(textfile) as infile:
    for line in infile:
        val = float(line.split()[2])
        voltage.append((val))
        time.append(float(line.split()[1]))
        detector_output.append(float(line.split()[3]))


print(voltage[500])
plt.plot(time[:2000],voltage[:2000])
plt.show()