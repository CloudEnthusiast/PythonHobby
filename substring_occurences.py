#!/usr/bin/env python
import re
main_string = raw_input("enter string:")
sub_string = raw_input("enter substring to be matched:")

mylist=re.findall(sub_string,main_string)
print mylist
print(len(mylist))
