#this is to show the results from the learner

import pandas as pd
import numpy as np
import fastai
from fastai.text import *
import pickle as pkl
import os
import sys

"""# Imports

Primeiro fazemos o import da wikipedia e do Sentiment 140
"""
local = "coleta/"
wikipedia = 1

cols = ['sentiment','id','date','query_string','user','text']
sent_140_test = pd.read_csv('testdata.manual.2009.06.14.csv', encoding='latin-1', header=None, names=cols)
sent_140_train = pd.read_csv('training.1600000.processed.noemoticon.csv', encoding='latin-1', header=None, names=cols)
print("loaded data sets")

#-------------------------------------------------
#LOAD DATA TRAIN TO DATA BUNCH

data = load_data(path='',file='only-sentiment-train-data.pkl', bs=48)

# DATA TEST

print("loading test data")

#this loads data test to a data bunch
test_datalist = TextList.from_df(sent_140_test, cols='text', vocab=data.vocab)

data_clas = load_data(path='',file='sentiment-test-data.pkl', bs=48)

#---------------------------------------------------------------

#Loads the trained model

print('trying to load')

learn = load_learner('trained_model')
print('loaded')

# PLACE ANALYSIS
local = "coleta/"
os.chdir(local) #change current directory
for directory in os.listdir():
    os.chdir(directory)
    os.chdir('vader') #acessa o diretorio vader
    df = pd.DataFrame()
    print('working on files from: ', (directory+'/vader/'))
    for file in os.listdir():	#get all files from this directory
    	if file.endswith(".npy"):
            path = os.getcwd()+ '/'+ file
            print('\t',file)
            tweets_df = np.load(path, allow_pickle=True).item()
            df = pd.DataFrame.from_dict(tweets_df, orient='index')
            df.assign(wiki=np.nan)
            for index, row in df.iterrows():
                one,two,three = learn.predict(row['text'])
                df.at[index,'wiki'] = one
        #break;
    #break;
            dicio = df.to_dict(orient='index') #saving process
            saving_path = os.getcwd()+'/'+'final/'+file
            np.save(saving_path, dicio)
    os.chdir('../..') #get back



print("done")
