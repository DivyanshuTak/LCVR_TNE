import numpy as np
import math as m

h_v = 0
ratio=0
l_r=0
delta=0
#retardence = input("enter the value of the retardence in degrees->")
polarisation = input("enter the polarisation->")
if polarisation == "linear":
    horv = input("enter horizontal or vertical")
    if horv == "horizontal":
        h_v = 1
    elif horv == "vertical":
        h_v = -1
elif polarisation == "circular":
    lorr = input("left or right")
    if lorr == "left":
        l_r = -1
    elif lorr  == "right":
        l_r = 1
elif polarisation == "elliptical":
   ratio = input("enter the fast axis to slow axis ratio ")

fi = input("enter the relative orientation of the retarder in degrees")

S = [1 , h_v , ratio , l_r]
c2 = (m.cos((m.radians(2*int(fi)))))
s2 = (m.sin((m.radians(2*int(fi)))))
print("input matrix is ",S)
while delta <= 180:
    cdel = (m.cos(m.radians(delta)))
    sdel = (m.sin(m.radians(delta)))
    M = np.array([[1, 0, 0, 0], [0, c2 * c2 + s2 * s2 * cdel, c2 * s2 * (1 - cdel), -s2 * sdel],
                  [0, c2 * s2 * (1 - cdel), s2 * s2 + c2 * c2 * cdel, c2 * sdel], [0, s2 * sdel, -c2 * sdel, cdel]])
    output = np.matmul(M,S)
    sdash = [int(output[0]),int(output[1]),int(output[2]),int(output[3])]
    if delta == 90:
        print("output matrix at delta = ", delta, "is :", sdash)
    elif delta==180:
        print("output matrix at delta = ", delta, "is :", sdash)
    delta += 10










