# this python script compares only 2 files(command line args)
# it simply ignores 3rd file if given.
import sys

# Specify the number of spaces between the columns
S = 4

if len(sys.argv)<3:
   print '\nSecond file name is needed to compare'
   sys.exit(0)

# Read the first file
f1 = open( sys.argv[1] ).read().split('\n')

# Read the second file
f2 = open( sys.argv[2] ).read().split('\n')

# Find the length of the longest line of the first file
n = len(max(f1, key=len))

# Print the lines
for i in  xrange( max(len(f1), len(f2)) ):

    try:
        print f1[i] + ' '*( n - len(f1[i]) + S) + f2[i]
    except:
        try:
            print ' ' + ' '*( n - 1 + S) + f2[i]
        except:
            print f1[i]
