#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Write a program to prompt for a file name, and then read through
#the file and look for lines of the form:

#X-DSPAM-Confidence: 0.8475

#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
#the line to extract the floating point number on the line. Count these lines and the
#compute the total of the spam confidence values from these lines. When you reach
#the end of the file, print out the average spam confidence.

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :continue
    pos = line.find (':')
    num = float(line[pos+1:])
    total = total+num
    count = count+1
avg = total/count
print "Average spam confidence:", avg
print "THE END"