#!/usr/bin/python
import sys
for line in sys.stdin:
	line = line.strip()
	try:	
		if line == '"tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"':
			continue
		else:
			word = line.split(',')
			# wordneeded = word[2],word[4],word[10],word[14],word[17],word[18],word[19]
			pickupdate = word[2][1:-1]
			date,time = pickupdate.split()
			date = date.split('-')
			date = ''.join(date)
			time = time.split(':')
			pickuptime = date+time[0]
		print pickuptime
	except:
		continue
		#word[5] = pickuptime
		#print '{0}'.format(word[5])
#		dropoffdate = word[6]
#		date,time = pickupdate.split(' ')
#		date = date.split('-')
#		date = ''.join(date)
#		time = time.split(':')
#		dropofftime = date+time[0]
#		word[6] = dropofftime
	