import sys
numOfStudents = 0
grades = [0,0,0,0,0,0,0,0,0,0,0]
id = ['','','','','','','','','','','']
sum = 0

data = open(sys.argv[1],'r')
data.next()
#recieve the input and parse it, one line at a time
for line in data:
  parsed = line.split(",")
  sum = sum + int(parsed[2])
  id[int(parsed[2])] += ", "+parsed[1]
  grades[int(parsed[2])] +=1
  numOfStudents +=1
  
data.close()

print "The avg is: "+str(float(sum)/float(numOfStudents))+"\n*****************\n"

i = 0
while (i < 11):
	print "%s studnets got %s points \n" %(grades[i], i)
	if (grades[i] > 0):
	  id[i] = id[i][1:] # remove the first ','
	  print "the list of every one who got %s : %s \n" %(i, id[i])
	print"**************************************\n"
	i +=1

