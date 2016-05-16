#!/usr/bin/python
import sys
for line in sys.stdin:
	line = line.strip()
	try:
		if line == 'VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,pickup_longitude,pickup_latitude,RateCodeID,store_and_fwd_flag,dropoff_longitude,dropoff_latitude,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount':
			continue
		else:
			word = line.split(',')
			# wordneeded = word[2],word[4],word[10],word[14],word[17],word[18],word[19]
			pickupdate = word[1]
			date,time = pickupdate.split()
			date = date.split('-')
			date = ''.join(date)
			time = time.split(':')
			pickuptime = date+time[0]
			longitude = int(((float(word[5])+74.035708)*10**6)/1470)
			latitude = int(((float(word[6])-40.695776)*10**6)/440)
			if longitude < 0 or latitude <0 or longitude > 73 or latitude >87:
				countinue
			longitude = str(longitude)
			latitude = str(latitude)
			if len(longitude) < 2: 
				longitude = '0'+ longitude
			if len(latitude) < 2:
				latitude = '0' + latitude
			tag = longitude+latitude
		print '{0}\t{1}'.format(pickuptime,tag)
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
	