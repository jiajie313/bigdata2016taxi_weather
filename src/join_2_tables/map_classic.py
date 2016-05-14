#!/usr/bin/python
import sys
import re
import os

# Classic Mapper without bin-hashing

key_idx_trip = [0, 1, 2, 5]
key_idx_fare = [0, 1, 2, 3]
key_idx = []
val_idx = []
file_flag = ''
file_name = os.environ.get("mapreduce_map_input_file")
if re.search('trip', file_name):
    key_idx = key_idx_trip
    file_flag = 'trip'
elif re.search('fare', file_name):
    key_idx = key_idx_fare
    file_flag = 'fare'
elif re.search('license', file_name):
    key_idx = key_idx_lics
    file_flag = 'lics'
else:
    pass

BUCKETS_AMNT = 10
BKT_ID_WIDTH = 3

for line in sys.stdin:
    if re.search('^medallion', line):
        continue
    info = line.strip().split(',')
    col_num = len(info)
    val_idx = [i for i in range(col_num) if i not in key_idx]
    key = [info[i] for i in key_idx]
    val = [info[i] for i in val_idx]
    key_str = ','.join(key)
    val_str = ','.join(val)
    ##
    ## Needs adaptation depending on input file_flag
    ##
    if (file_flag == 'trip'): # stay left
        print "%s\t%s,%s" % (key_str, file_flag, val_str)
    elif (file_flag == 'fare'): # stay right
        print "%s\t%s,%s" % (key_str, file_flag, val_str)
    else:
        continue


