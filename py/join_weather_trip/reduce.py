#!/usr/bin/python
import sys


for line in sys.stdin:
    line = line.strip()
    word = line.split(',')


    key_tag, values = line.strip().split('&', 1)
    key, tag = key_tag.strip().split('\t', 1)
    word

    date = word[0:8].replace('/', ',')






    try:
        if key != current_key:    
            if isFirst == 0:
                for trip in tripList:
                    for fare in fareList:
                        print"{0}\t{1},{2}".format(trip[0],trip[1],fare[1])
            else:
                isFirst =0 
            current_key = key
            fareList = []
            tripList = []
        if tag == 'fare':
            fareList.append([key,values])
        else:
            tripList.append([key,values])
    except:
        pass
 
try:
    for trip in tripList:
        for fare in fareList:
            print"{0}\t{1},{2}".format(trip[0],trip[1],fare[1])
except:
    pass