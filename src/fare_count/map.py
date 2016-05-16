#!/usr/bin/python
import sys
import re
import os

# Similar to word-count
# Mapper: <range_str> \t <1>
# In-mapping combiner

def Fare2RangeStr(x):
    res = None
    try:
        x = float(x)
    except ValueError:
        res = 'error-value'
    # range lower~upper pair ([48.01 , infinite] absent so far)
    rg_lw = range(0, 48, 4)
    rg_up = [i + 4 for i in rg_lw]
    rg_lw_max = rg_up[-1] + 0.01
    rg_lw = [rg_lw[0]] + [i + 0.01 for i in rg_lw[1:]]
    for i in range(len(rg_lw)):
        i_lw = rg_lw[i]
        i_up = rg_up[i]
        if (x >= i_lw and x <= i_up):
            res = "%s,%s" % (str(i_lw), str(i_up))
            break
    if ((not res) and x >= rg_lw_max):
        res = "%s,%s" % (str(rg_lw_max), 'infinite')

    # unknown dirty-data source
    if (x < 0): # negative fare value
        res = 'error-neg'
    if not res: # dirty-data
        res = 'error-unknown2'
    return(res)

FARE_INDEX = 12
COUNT_BASIC = 1

DICT = {}
for line in sys.stdin:
    if not line.strip():
        continue
    if re.search('^vendor_id', line):
        continue
    info = line.strip().split(',')
    fare_num = info[FARE_INDEX]
    fare_rg_str = Fare2RangeStr(fare_num)
    try:
        DICT[fare_rg_str] += COUNT_BASIC
    except KeyError:
        DICT[fare_rg_str] = COUNT_BASIC

for k, v in DICT.iteritems():
    print "%s\t%d" % (k, v)


