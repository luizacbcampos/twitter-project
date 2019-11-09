#!/usr/bin/env bash

## automate queries from file
TYPE=$1
LABEL=$2
MONTH_YEAR=$3
N_THREADS=$4

start=$SECONDS
echo "organizing ${TYPE}/${MONTH_YEAR}/${LABEL} ... "
./organize-tweets.py "${TYPE}" "${LABEL}" "${MONTH_YEAR}" ${N_THREADS}
duration=$(( SECONDS - start))
echo "organized ${TYPE}/${MONTH_YEAR}/${LABEL} ... total time elapsed: "$duration" seconds"
echo
