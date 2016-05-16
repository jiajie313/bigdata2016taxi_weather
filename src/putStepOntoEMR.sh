#!/usr/bin/env bash

# aws emr add-steps --cluster-id j-3K7UIS0LKDNFP \
# --steps Type=STREAMING,Name="SubWordCount2",ActionOnFailure=CONTINUE,\
# Args=[-files,"",-mapper,map.py,-reducer,reduce.py,-input,s3://spring-2016-bigdata-yy1533/wordcount/input/,-input,s3://spring-2016-bigdata-yy1533/wordcount/wikipedia2.txt,-output,s3://spring-2016-bigdata-yy1533/wordcount/output2/]

CID=$1
JSON=$2
# CID=j-OKD6HB8Y12WI
aws emr add-steps --cluster-id $CID --steps file://$JSON

# [
#   {
#      "Name": "SubWordCount2Json",
#      "Type": "STREAMING",
#      "ActionOnFailure": "CONTINUE",
#      "Args": [
#          "-files",
#          "s3://spring-2016-bigdata-yy1533/wordcount/map.py,s3://spring-2016-bigdata-yy1533/wordcount/reduce.py",
#          "-mapper",
#          "map.py",
#          "-reducer",
#          "reduce.py",
#          "-input",
#          "s3://spring-2016-bigdata-yy1533/wordcount/wikipedia2.txt",
#          "-output",
#          "s3://spring-2016-bigdata-yy1533/wordcount/output2/"]
#   }
# ]