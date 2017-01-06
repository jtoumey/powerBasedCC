OUTFILENAME = "outputTest.dat"

class sample:
   time      = 0.0
   heartRate = 0
   power     = 0

t0 = sample()

t0.time = 1.553
t0.heartRate = 156
t0.power = 185


# Open the file and write the data to it
outputFile = open(OUTFILENAME, 'w')

outputFile.write("# Sampled Data\n")
outputFile.write("# time (sec)   heart rate (BPM)   power (Watt)\n")
outputFile.write("{} {} {}\n".format(t0.time, t0.heartRate, t0.power))

outputFile.close()
