import numpy as np
import pandas as pd
import re
import string

other_chars = ['...','…','..','.. ..']

# text cleaner (individual)
def tweet_text_cleaner(x):
    # remove other characters
    x_out = x.replace(u'\xa0', u' ')
    for i in other_chars:
        x_out = x_out.replace(i,'')
    # replace multiple spaces into one spaces
    x_out = re.sub(' +',' ',x_out)
    # remove newline characters
    x_out = re.sub(r'\n+',' ',x_out)
    # remove hyperlinks
    x_out = re.sub(r'http:\/\/\s','http://',x_out)
    x_out = re.sub(r'https:\/\/\s','https://',x_out)
    x_out = re.sub(r'https?:\/\/.*\/\w*','',x_out)
    # remove twitter picture hyperlinks
    x_out = re.sub(r'pic.twitter.com\/\w*','',x_out)
    # remove user mentions
    x_out_um_space = re.findall(r'(@\s[\w_-]+)',x_out)
    x_out_um_nospace = re.findall(r'(@[\w_-]+)',x_out)
    x_out_um = x_out_um_space+x_out_um_nospace
    for i, j in enumerate(x_out_um):
        x_out_um[i] = j.replace(' ','')
    x_out = re.sub(r'(@\s[\w_-]+)','',x_out)
    x_out = re.sub(r'(@[\w_-]+)','',x_out)
    # match hashtags
    x_out_ht_space = re.findall(r'(#\s[\w_-]+)',x_out)
    x_out_ht_nospace = re.findall(r'(#[\w_-]+)',x_out)
    x_out_ht = x_out_ht_space+x_out_ht_nospace
    for i, j in enumerate(x_out_ht):
        x_out_ht[i] = j.replace(' ','').lower() # lowercase the hashtags
    x_out = x_out.replace('# ','#')

    return x_out, x_out_ht, x_out_um

# time splitter (individual)
def time_split(x,by='month'):
    x_split = x.split(' ')
    date = x_split[0]
    time = x_split[1]
    date_split = date.split('-')
    time_split = time.split(':')
    time_vect = date_split + time_split
    out_time = []
    if by == 'year':
        out_time = [int(i) for i in time_vect[0:1]]
    elif by == 'month':
        out_time = [int(i) for i in time_vect[0:2]]
    elif by == 'day':
        out_time = [int(i) for i in time_vect[0:3]]
    elif by == 'hour':
        out_time = [int(i) for i in time_vect[0:4]]
    return out_time

# time binner (whole)
def time_binner(T,by='month'):
    month_code = {'01':1,'02':2,'03':3,'04':4,'05':5,'06':6,'07':7,'08':8,'09':9,'10':10,'11':11,'12':12}
    month_range = {1:[1,31],2:[1,28],3:[1,31],4:[1,30],5:[1,31],6:[1,30],7:[1,31],8:[1,31],9:[1,30],10:[1,31],11:[1,30],12:[1,31]}
    leap_years = [2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]
    month_range_leap = {1:[1,31],2:[1,29],3:[1,31],4:[1,30],5:[1,31],6:[1,30],7:[1,31],8:[1,31],9:[1,30],10:[1,31],11:[1,30],12:[1,31]}

    time_txt = T['datetime']

    time_data = []
    for i in list(time_txt.keys()):
        time = time_txt[i]
        time_split = time.split(' ')
        date = time_split[0]
        date_split = date.split('-')
        time_data.append(date_split)
    time_data = pd.DataFrame(np.matrix(time_data,dtype=int),columns=['year','month','day'],index=time_txt.keys())

    Yu = np.unique(time_data['year'])
    Mu = np.unique(time_data['month'])
    Du = np.unique(time_data['day'])

    bins_on = {}
    for i in range(Yu.min(),Yu.max()+1):
        for jj ,j in enumerate(range(Mu.min(),Mu.max()+1)):
            if by == 'year':
                bins_on[i] = []
            elif by == 'month':
                bins_on[i,j] = []
            elif by == 'day':
                if len(Du) == 1:
                    minimum = Du[0].min()
                    maximum = Du[0].max()+1
                else:
                    if i not in leap_years:
                        MR = month_range
                    else:
                        MR = month_range_leap

                    if jj == 0:
                        minimum = Du[jj].min()
                        maximum = MR[j][1]+1
                    elif jj == len(Du)-1:
                        minimum = MR[j][0]
                        maximum = Du[jj].max()+1
                    else:
                        minimum = MR[j][0]
                        maximum = MR[j][1]+1
                for k in range(minimum,maximum):
                    bins_on[i,j,k] = []

    # populate bins
    for i in list(time_data.T.keys()):
        time_stamp = list(time_data.T[i].values)
        if by == 'year':
            bins_on[time_stamp[0]].append(i)
        elif by == 'month':
            bins_on[time_stamp[0],time_stamp[1]].append(i)
        elif by == 'day':
            bins_on[time_stamp[0],time_stamp[1],time_stamp[2]].append(i)

    # count bin populations
    bins_on_count = {}
    for i in bins_on.keys():
        length = len(bins_on[i])
        bins_on_count[i] = length

    return bins_on, bins_on_count