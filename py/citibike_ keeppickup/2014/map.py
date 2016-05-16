#!/usr/bin/python
import sys
for line in sys.stdin:
	line = line.strip()
	try:	
		if line == '"tripduration","starttime","stoptime","start station id","start station name","start station latitude","start station longitude","end station id","end station name","end station latitude","end station longitude","bikeid","usertype","birth year","gender"':
			continue
		else:
			word = line.split()
			# wordneeded = word[2],word[4],word[10],word[14],word[17],word[18],word[19]
			pickupdate = word[0][0:-2]
			date = pickupdate.split('/')
			if len(date)==1:
				date = date
				time = ''
			else:
				date = date[2]+date[0]+date[1]
				time = word[0][-2:]
			pickuptime = date+time
		print '{0}\t{1}'.format(pickuptime,word[1])
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
	