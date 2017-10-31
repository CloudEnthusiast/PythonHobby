#!/usr/bin/env python

'''i
the user enters a string and interger value as a spliter.This program will print the output by removing any subsequent occurrences of non-distinct characters

Input:
AABCAAADA
3
Output:
AB
CA
AD
Explanation of problem: String AABCAAADA will be divided into 3 sub_string as AAB, CAA, ADA and output will be printed as AB, CA, AD by removing repeatative elements of the sub_string.

'''
import re

def itersplit_into_x_chunks(string,x=10): # we assume here that x is an int and > 0
    size = len(string)
    chunksize = size//x #floor division
    for pos in range(0, size, chunksize):
        yield string[pos:pos+chunksize]

main_string = raw_input("enter string:")
val = int(raw_input("enter split size:"))

mylist = list(itersplit_into_x_chunks(main_string,val))
print (mylist)

for str in mylist:
    print ''.join([j for i,j in enumerate(str) if j not in str[:i]]),
