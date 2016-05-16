#!/usr/bin/python
import sys
import re
import os

# Reducer
# Same as classic reducer.py

cached_key = None
cached_sum = 0
for line in sys.stdin:
    stream_key, stream_num = line.strip().split('\t')
    if (re.search('error', stream_key)):
        continue
    try:
        stream_num = int(stream_num)
    except ValueError:
        continue

    if cached_key == stream_key:
        cached_sum += stream_num
    else:
        if cached_key:
            print "%s\t%d" % (cached_key, cached_sum)
        cached_key = stream_key
        cached_sum = stream_num

# end of stream
if cached_key:
    print "%s\t%d" % (cached_key, cached_sum)

