#!/usr/bin/python
import sys
	for line in sys.stdin:
		line = line.strip()
		
	if line == '  USAF  WBAN YR--MODAHRMN DIR SPD GUS CLG SKC L M H  VSB MW MW MW MW AW AW AW AW W TEMP DEWP    SLP   ALT    STP MAX MIN PCP01 PCP06 PCP24 PCPXX SD':
		continue
	elif len(line) == 14:
		word = line.split(',')
		# wordneeded = word[2],word[4],word[10],word[14],word[17],word[18],word[19]
		pickupdate = word[5]
		date,time = pickupdate.split(' ')
		date = date.split('/')
		if int(date[0])<10:
			date[0] = '0'+date[0]
		if int(date[1])<10:
			date[1] = '0'+date[1]
		date = date[2]+date[0]+date[1]
		time = time.split(':')
		if time[0]<10:
			time[0] = '0'+time[0]
		time = time[0]+time[1]
		pickuptime = date+time
		word[5] = pickuptime

		dropoffdate = word[6]
		date,time = pickupdate.split(' ')
		date = date.split('/')
		if int(date[0])<10:
			date[0] = '0'+date[0]
		if int(date[1])<10:
			date[1] = '0'+date[1]
		date = date[2]+date[0]+date[1]
		time = time.split(':')
		if time[0]<10:
			time[0] = '0'+time[0]
		time = time[0]+time[1]
		dropofftime = date+time
		word[6] = dropofftime
		
		line = '\t'.join(word)
	print line