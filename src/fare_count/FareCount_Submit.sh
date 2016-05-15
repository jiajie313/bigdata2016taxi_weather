#!/usr/bin/env bash

myarray=( 100 10000 100000 1000000 2000000 4000000 8000000 15000000 )
s3site="s3://spring-2016-bigdata-yy1533/performance"
TaskPrefix=Perf_FareCount
FilePrefix=yellow_tripdata_2013-01.csv
FilePrefix2=yellow_tripdata_2013-02.csv
Cid=j-OKD6HB8Y12WI
MapperNum=10
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
        MapperNum=5
    else
        MapperNum=10
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
         \"mapreduce.job.reduces=1\",
         \"-D\",
         \"mapreduce.job.maps=$MapperNum\",     
         \"-files\",
         \"$s3site/src/fare_count/map_classic.py,$s3site/src/fare_count/reduce_classic.py\",
         \"-mapper\",
         \"map_classic.py\",
         \"-reducer\",
         \"reduce_classic.py\",
         \"-input\",
         \"$s3site/taxi_data/${FilePrefix}.$item\",
         \"-output\",
         \"$s3site/output/${SchemeName}.$item.count\"]
  }
]
" > ${SchemeName}_$item.json

sh ../putStepOntoEMR.sh $Cid ${SchemeName}_$item.json
done

echo Find File Size: 30000000
echo "
[
  {
     \"Name\": \"${SchemeName}_30000000\",
     \"Type\": \"STREAMING\",
     \"ActionOnFailure\": \"CONTINUE\",
     \"Args\": [
         \"-D\",
         \"mapreduce.job.reduces=1\",
         \"-D\",
         \"mapreduce.job.maps=$MapperNum\",     
         \"-files\",
         \"$s3site/src/fare_count/map_classic.py,$s3site/src/fare_count/reduce_classic.py\",
         \"-mapper\",
         \"map_classic.py\",
         \"-reducer\",
         \"reduce_classic.py\",
         \"-input\",
         \"$s3site/taxi_data/${FilePrefix}\",
         \"-input\",
         \"$s3site/taxi_data/${FilePrefix2}\",
         \"-output\",
         \"$s3site/output/${SchemeName}.30000000.count\"]
  }
]
" > ${SchemeName}_30000000.json
sh ../putStepOntoEMR.sh $Cid ${SchemeName}_30000000.json

##
## Part-2: Running In-Mapper Combiner Scheme
##
SchemeName=${TaskPrefix}_InMCombiner
echo Scheme: $SchemeName
for i in ${!myarray[@]}
do
    if [[ $i < 5 ]]; then
        MapperNum=5
    else
        MapperNum=10
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
         \"mapreduce.job.reduces=1\",
         \"-D\",
         \"mapreduce.job.maps=$MapperNum\",     
         \"-files\",
         \"$s3site/src/fare_count/map_classic.py,$s3site/src/fare_count/reduce_classic.py\",
         \"-mapper\",
         \"map_classic.py\",
         \"-reducer\",
         \"reduce_classic.py\",
         \"-input\",
         \"$s3site/taxi_data/${FilePrefix}.$item\",
         \"-output\",
         \"$s3site/output/${SchemeName}.$item.count\"]
  }
]
" > ${SchemeName}_$item.json

# sh ../putStepOntoEMR.sh $Cid ${SchemeName}_$item.json
done

echo Find File Size: 30000000
echo "
[
  {
     \"Name\": \"${SchemeName}_30000000\",
     \"Type\": \"STREAMING\",
     \"ActionOnFailure\": \"CONTINUE\",
     \"Args\": [
         \"-D\",
         \"mapreduce.job.reduces=1\",
         \"-D\",
         \"mapreduce.job.maps=$MapperNum\",     
         \"-files\",
         \"$s3site/src/fare_count/map.py,$s3site/src/fare_count/reduce.py\",
         \"-mapper\",
         \"map.py\",
         \"-reducer\",
         \"reduce.py\",
         \"-input\",
         \"$s3site/taxi_data/${FilePrefix}\",
         \"-input\",
         \"$s3site/taxi_data/${FilePrefix2}\",
         \"-output\",
         \"$s3site/output/${SchemeName}.30000000.count\"]
  }
]
" > ${SchemeName}_30000000.json
# sh ../putStepOntoEMR.sh $Cid ${SchemeName}_30000000.json

