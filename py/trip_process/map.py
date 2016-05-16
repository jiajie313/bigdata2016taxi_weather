#!/usr/bin/python
import sys
	for line in sys.stdin:
		line = line.strip()
		
	if line == 'medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_datetime,dropoff_datetime,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude':
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
		pickuptime = date+time[0]
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
		dropofftime = date+time[0]
		word[6] = dropofftime
		
		
		print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}'.format(word[0],word[5],word[6],word[7],word[8],word[9],word[10],word[11],word[12],word[13])