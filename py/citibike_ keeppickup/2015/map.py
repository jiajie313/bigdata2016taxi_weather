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
			pickupdate = word[0]
			date = pickupdate.split('/')
			if not date[0]:
				continue
			if len(date)==1:
				date = date
				time = ''
			else:
				time = date[2][4:]
				if len(date[0])<2:
					date[0]='0'+date[0]
				if len(date[1])<2:
					date[1]='0'+date[1]
				if len(time)<2:
					time = '0'+time
				date = date[2][:4]+date[0]+date[1]
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
	