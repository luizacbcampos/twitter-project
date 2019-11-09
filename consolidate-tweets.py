#!/usr/bin/env python3

##!/home/aquijano4/miniconda3/bin/python

import sys
import os
import json
import shutil

TYPE = sys.argv[1]
LABEL = sys.argv[2]

PATH = TYPE+'/'+LABEL+'/'
PATH_DATA = PATH+'Data/tweet'

print('Consolidating files for '+PATH+'...')
with open(PATH+LABEL+'.json','a') as out_file:
	for i in os.scandir(PATH_DATA):
		with open(i.path) as in_file:
			tweet = json.load(in_file)
			json.dump(tweet,out_file)
			out_file.write('\n')
		os.remove(i.path)
os.system("awk '!seen[$0]++' "+PATH+LABEL+".json > "+PATH+LABEL+"-u.json")
os.system("rm "+PATH+LABEL+".json")
os.system("mv "+PATH+LABEL+"-u.json "+PATH+LABEL+".json")
shutil.rmtree(PATH+'Data/')
os.remove(PATH+'scrapy.cfg')
shutil.rmtree(PATH+'TweetScraper/')
print('Finished consolidating files.')