import os
import subprocess

filepath = "E:\dnNIDLL"
file = "LCVRRESPONSE.exe"
p=subprocess.Popen(os.path.join(filepath,file))
#os.startfile(os.path.join(filepath,file))
print("next_process is started")
print(10*50)
poll = p.poll()
print(poll)
while poll==None:
    poll = p.poll()
print("process completed")
while True:
    print("y")