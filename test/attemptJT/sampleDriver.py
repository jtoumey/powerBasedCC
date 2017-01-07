IDX = 12

# Import class definitions from the class definition file
import classDef

# Initialize a list of objects 
sampleList = []


for i in range(IDX):
   # Initialize an object
   t = classDef.sample() 
   # Assign the time as the current iteration counter
   t.time = i*i
   sampleList.append(t)




for i in range(IDX):
   print("{}".format(sampleList[i].time))
