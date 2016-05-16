#!/usr/bin/env bash

myarray=( 100 1K 10K 50K 100K 200K 400K 800K 1M 1p5M 2M )
s3site="s3://spring-2016-bigdata-yy1533/performance"
TaskPrefix=Perf_JoinTripFare
FareFileName=fare_data_week1.csv
Cid=j-2KP7E2UNPT6TM
MapperNum=5
# -D mapreduce.job.reduces=2

#
# Note: different mapper/reducer pairs
#

#
# Part-1: Running Classic Scheme
#
SchemeName=${TaskPrefix}_Classic
echo Scheme: $SchemeName
for i in ${!myarray[@]}
do
    if [[ $i < 5 ]]; then
        MapperNum=10
    else
        MapperNum=20
    fi
    item=${myarray[$i]}
echo Find File Size: $item
echo "
[
  {
     \"Name\": \"${SchemeName}_$item\",
     \"Type\": \"STREAMING\",
     \"ActionOnFailure\": \"CONTINUE\",
     \"Args\": [
         \"-D\",
         \"mapreduce.job.reduces=5\",
         \"-D\",
         \"mapreduce.job.maps=$MapperNum\",     
         \"-files\",
         \"$s3site/src/join_2_tables/map_classic.py,$s3site/src/join_2_tables/reduce_classic.py\",
         \"-mapper\",
         \"map_classic.py\",
         \"-reducer\",
         \"reduce_classic.py\",
         \"-input\",
         \"$s3site/data/$FareFileName,$s3site/data/trip_data_$item.csv\",
         \"-output\",
         \"$s3site/output/${SchemeName}_$item.txt\"]
  }
]
" > ${SchemeName}_$item.json

sh ../putStepOntoEMR.sh $Cid ${SchemeName}_$item.json
done

##
## Part-2: Running Bin-Hash Scheme
##
SchemeName=${TaskPrefix}_Bin
echo Scheme: $SchemeName
for i in ${!myarray[@]}
do
    if [[ $i < 5 ]]; then
        MapperNum=10
    else
        MapperNum=20
    fi
    item=${myarray[$i]}
echo Find File Size: $item
echo "
[
  {
     \"Name\": \"${SchemeName}_$item\",
     \"Type\": \"STREAMING\",
     \"ActionOnFailure\": \"CONTINUE\",
     \"Args\": [
         \"-D\",
         \"mapreduce.job.reduces=5\",
         \"-D\",
         \"mapreduce.job.maps=$MapperNum\",     
         \"-files\",
         \"$s3site/src/join_2_tables/map.py,$s3site/src/join_2_tables/reduce.py\",
         \"-mapper\",
         \"map.py\",
         \"-reducer\",
         \"reduce.py\",
         \"-input\",
         \"$s3site/data/$FareFileName,$s3site/data/trip_data_$item.csv\",
         \"-output\",
         \"$s3site/output/${SchemeName}_$item.txt\"]
  }
]
" > ${SchemeName}_$item.json

sh ../putStepOntoEMR.sh $Cid ${SchemeName}_$item.json
done