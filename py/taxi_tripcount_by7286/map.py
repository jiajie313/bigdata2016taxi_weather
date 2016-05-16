#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
 	word = line.strip().split('\t')
 	word = word[0] + word [1]
	#print line 
	print "%s\t%d" %(word, 1 )  
   # l = line.strip().split()
    
   # for word in l:
        
        # output goes to STDOUT (stream data that the program writes)
   #     print "%s\t%d" %( word, 1 )