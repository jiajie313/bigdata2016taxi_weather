#!/usr/bin/python
import sys
	for line in sys.stdin:
		line = line.strip()
		word = line.split(',')
	if line == 'tripduration,starttime,stoptime,start station id,start station name,start station latitude,start station longitude,end station id,end station name,end station latitude,end station longitude,bikeid,usertype,birth year,gender':
		continue
	elif line == '  USAF  WBAN YR--MODAHRMN DIR SPD GUS CLG SKC L M H  VSB MW MW MW MW AW AW AW AW W TEMP DEWP    SLP   ALT    STP MAX MIN PCP01 PCP06 PCP24 PCPXX SD'
	elif len(word) == 14 or 33:
		print '{0}\t%d'.format(word[1],1)
