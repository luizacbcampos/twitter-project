#!/usr/bin/env bash

## automate queries from file
TYPE=$1
LABEL=$2
keyword=$3
YEAR=$4
MONTH=$5

start=$SECONDS
./scrape-tweets.sh "${TYPE}" "${LABEL}" "${keyword}" ${YEAR} ${MONTH}
duration=$(( SECONDS - start))
echo
