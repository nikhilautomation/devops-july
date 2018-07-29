#!/usr/bin/python

counter = 0
fh = open("testfile.txt","w+")
while(counter < 100):
    line = "User%d" %counter
    fh.write(line)

fh.close()
print("CHANGED FILE")    
