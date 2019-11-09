#!/usr/bin/env bash

TYPE=$1
LABEL=$2

start=$SECONDS
./consolidate-tweets.py ${TYPE} ${LABEL}
duration=$(( SECONDS - start))
echo
