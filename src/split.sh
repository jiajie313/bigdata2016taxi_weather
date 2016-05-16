#!/usr/bin/env bash

#myarray=( 100 1K 10K 50K 100K 200K 400K 800K 1M 1p5M 2M )
myarray=( 100 10000 100000 1000000 2000000 4000000 8000000 15000000 )

# myarray=(1 5)

File=yellow_tripdata_2013-01.csv

for i in ${!myarray[@]}
do
item=${myarray[$i]}

head -${item} $File > $File.$item

done
