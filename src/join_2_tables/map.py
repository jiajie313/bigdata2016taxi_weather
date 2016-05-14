#!/usr/bin/python
import sys
import re
import os

# Task1: trip x fare
# Mapper:
# revised mapper:
# val_str will be hashed into buckets
# <key_str><bucket_file_a><bucket_file_b> \t <file_flag> , <val_str>

def Str2BucketID(s, b = 100):
    # string -> binary -> int_sum -> bucket_num
    # s: string
    # b: number of buckets
    # return: int of bucket id in [0, b) e.g. 'hello' -> 32
    res = 0
    BASE_NUM = b
    s = str(s)
    bin_list = [format(ord(char), 'b') for char in s]
    int_sum = sum([int(bit_num, 2) for bit_num in bin_list]) + BASE_NUM
    res = int_sum % b
    return res

def FormatInt2Str(x, width = 3, fill_char = '0'):
    # 1 -> 001
    x = int(x)
    res = '{num:{fill}{width}}'.format(num = x, fill = fill_char, width = width)
    return res

def FormatNum2Char(s):
    # 0 -> a; 1 -> b; ... ; 9 -> j
    s = s.replace('0', 'a')
    s = s.replace('1', 'b')
    s = s.replace('2', 'c')
    s = s.replace('3', 'd')
    s = s.replace('4', 'e')
    s = s.replace('5', 'f')
    s = s.replace('6', 'g')
    s = s.replace('7', 'h')
    s = s.replace('8', 'i')
    s = s.replace('9', 'j')
    return(s)


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
    val_bkt = Str2BucketID(val_str, b = BUCKETS_AMNT)
    val_bkt_id = FormatNum2Char(FormatInt2Str(val_bkt, BKT_ID_WIDTH))
    ##
    ## Needs adaptation depending on input file_flag
    ##
    if (file_flag == 'trip'): # stay left
        for tmp in range(BUCKETS_AMNT):
            tmp_bkt_id = FormatNum2Char(FormatInt2Str(tmp, BKT_ID_WIDTH))
            print "%s%s%s\t%s,%s" % (key_str, val_bkt_id, tmp_bkt_id, file_flag, val_str)
    elif (file_flag == 'fare'): # stay right
        for tmp in range(BUCKETS_AMNT):
            tmp_bkt_id = FormatNum2Char(FormatInt2Str(tmp, BKT_ID_WIDTH))
            print "%s%s%s\t%s,%s" % (key_str, tmp_bkt_id, val_bkt_id, file_flag, val_str)
    else:
        continue


