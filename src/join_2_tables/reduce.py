#!/usr/bin/python
import sys
# import itertools as it

# Revised
# Task1
# Reducer: <key_str> \t <tuple1> , <tuple2>
# Mapper:
# <key_str><bucket_file_a><bucket_file_b> \t <file_flag> , <val_str>

def PrintJoin(listA, listB, leader):
    for a in listA:
        for b in listB:
            print "%s\t%s,%s" % (leader, a, b)

stream_key_str = ""
stream_val_str = ""
file_flag = ""

cached_key_str = None
cached_bkt_str = None
cached_val_str_a = []
cached_val_str_b = []
join_val_str = []

BKT_ID_WIDTH = 3

for line in sys.stdin:
    # stream_key_str, stream_bkt_str, info = line.strip().split('\t')
    stream_key_str, info = line.strip().split('\t', 1)

    # print [stream_key_str, stream_bkt_str, info[:10]]
    file_flag, stream_val_str = info.split(',', 1)

    # if (stream_key_str == cached_key_str and stream_bkt_str == cached_bkt_str):
    if (stream_key_str == cached_key_str):
        # matched key
        if (file_flag == 'trip'):
            # tuple from 'trip' stayed left
            cached_val_str_a.append(stream_val_str)
        elif (file_flag == 'fare'):
            # tuple from 'fare' stayed right
            cached_val_str_b.append(stream_val_str)
        else:
            pass
    else:
        # unseen key
        # if (cached_key_str and cached_bkt_str):
        if (cached_key_str):
            # join_val_str = [cached_val_str_a, cached_val_str_b]
            # for line in it.product(*join_val_str):
            #     print "%s\t%s,%s" % (cached_key_str, line[0], line[1])
            if (len(cached_val_str_a) > 0 and len(cached_val_str_b) > 0):
                cached_key_str = cached_key_str[0:len(cached_key_str)-2*BKT_ID_WIDTH]
                PrintJoin(cached_val_str_a, cached_val_str_b, cached_key_str)
        cached_key_str = stream_key_str
        # cached_bkt_str = stream_bkt_str
        # join_val_str = []
        cached_val_str_a =[]
        cached_val_str_b = []
        if (file_flag == 'trip'):
            cached_val_str_a = [stream_val_str]
        elif (file_flag == 'fare'):
            cached_val_str_b = [stream_val_str]
        else:
            pass

# end of line
# join_val_str = [cached_val_str_a, cached_val_str_b]
if (cached_key_str):
    if (len(cached_val_str_a) > 0 and len(cached_val_str_b) > 0):
        cached_key_str = cached_key_str[0:len(cached_key_str)-2*BKT_ID_WIDTH]
        PrintJoin(cached_val_str_a, cached_val_str_b, cached_key_str)
