IDX = 12

import time
# Import class definitions from the class definition file
import classDef

# Initialize a list of objects 
sampleList = []


for i in range(IDX):
   # Initialize an object
   t = classDef.sample() 
   # Assign the time as the current iteration counter
   t.time = i*i
   t.heartRate = i + 140
   t.power = i*10 +43
   sampleList.append(t)




for i in range(IDX):
   print("{}".format(sampleList[i].time))


timestr = time.strftime("%Y-%m-%d-%H-%M")
timestr += ".dat"

outputFile = open(timestr, 'w')

# Print a file header
outputFile.write("# Sampled Data\n")
outputFile.write("# time (sec)   heart rate (BPM)   power (Watt)\n")

for i in range(IDX):
   outputFile.write("{} {} {}\n".format(sampleList[i].time, sampleList[i].heartRate, sampleList[i].power))

outputFile.close()
