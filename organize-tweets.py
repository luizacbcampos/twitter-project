#!/usr/bin/env python3

##!/home/[username]/miniconda3/bin/python

import numpy as np
import json
import os
from joblib import Parallel, delayed
import sys
from process import tweet_text_cleaner, time_split

# label
TYPE = sys.argv[1]
LABEL = sys.argv[2]
MONTH_YEAR = sys.argv[3]

print('You are loading folder: ', MONTH_YEAR)

# number of threads
n_threads = int(sys.argv[4])

# directories
dir_0 = TYPE+'/'+ MONTH_YEAR + '/'+LABEL+'/'
dir_1 = TYPE+'-processed/'
try:
    dir_1 = dir_1 + MONTH_YEAR + '/'
    os.mkdir(dir_1)
except:
    pass

import time

dir_1 = TYPE+'-processed/' + MONTH_YEAR + '/'

def organizer(json_object,main_storage,bin_storage):
    try:
        # load json object
        json_file_i = json.loads(json_object)

        # clean texts
        txts, hts, ums = tweet_text_cleaner(json_file_i['text'])

        # split time
        year_month = time_split(json_file_i['datetime'],by='day')

        # populate bins
        try:
            bin_storage[year_month[0],year_month[1],year_month[2]].append(int(json_file_i['ID']))
        except:
            bin_storage[year_month[0],year_month[1],year_month[2]] = [int(json_file_i['ID'])]

        # populate data
        main_storage[int(json_file_i['ID'])] = {}
        main_storage[int(json_file_i['ID'])]['usernameTweet'] = json_file_i['usernameTweet']
        main_storage[int(json_file_i['ID'])]['text'] = txts
        main_storage[int(json_file_i['ID'])]['hashtags'] = ','.join(hts)
        main_storage[int(json_file_i['ID'])]['usermentions'] = ','.join(ums)
        main_storage[int(json_file_i['ID'])]['nbr_favorite'] = json_file_i['nbr_favorite']
        main_storage[int(json_file_i['ID'])]['nbr_reply'] = json_file_i['nbr_reply']
        main_storage[int(json_file_i['ID'])]['datetime'] = json_file_i['datetime']
        main_storage[int(json_file_i['ID'])]['is_reply'] = json_file_i['is_reply']
        main_storage[int(json_file_i['ID'])]['is_retweet'] = json_file_i['is_retweet']
        main_storage[int(json_file_i['ID'])]['user_id'] = json_file_i['user_id']
    except:
        pass

tweets_storage = {}
bins_storage= {}

print("\t\t"+dir_1+LABEL+'-tweets.npy')

with open(dir_0+LABEL+'.json','r') as in_file:
    Parallel(n_jobs=n_threads,backend='threading')(delayed(organizer)(i,tweets_storage,bins_storage) for i in in_file)

np.save(dir_1+LABEL+'-tweets.npy',tweets_storage)
np.save(dir_1+LABEL+'-bins.npy',bins_storage)
