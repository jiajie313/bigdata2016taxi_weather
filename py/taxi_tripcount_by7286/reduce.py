#!/usr/bin/python

import sys

current_word = None
current_sum = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    info = line.strip().split('\t')
   # word = word[0]+word[1]
    word = info[0]
    count = info[1]
    try:
        count = int(count)
    except ValueError:
        continue
    
    if word == current_word:
        current_sum += count
    else:
        if current_word:
            # output goes to STDOUT (stream data that the program writes)
            datehr = current_word[:10]
            tag = current_word[10:]
            print "%s\t%s\t%d" %( datehr, tag , current_sum )
        current_word = word
        current_sum = count