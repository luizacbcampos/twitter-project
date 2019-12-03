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

test_datalist = TextList.from_df(sent_140_test, cols='text', vocab=data.vocab)

'''
data_clas = (TextList.from_df(sent_140_train, cols='text', vocab=data.vocab)
             .split_by_rand_pct(0.2)
             .label_from_df(cols= 'sentiment')
             .add_test(test_datalist)
             .databunch(bs=32))
'''
data_clas = load_data(path='',file='sentiment-test-data.pkl', bs=48)
#data_clas.save('sentiment-test-data.pkl')
print("saved test data")

#---------------------------------------------------------------

#LEARNING PART AND ETC

print("wiki learning")

learn_classifier = text_classifier_learner(data_clas, AWD_LSTM, drop_mult=0.5)

# load the encoder saved
learn_classifier.load_encoder('wiki-train-data')
print("LOADEDD")

# select the appropriate learning rate
learn_classifier.lr_find()

# we typically find the point where the slope is steepest
learn_classifier.recorder.plot(return_fig=True)

# Fit the model based on selected learning rate
learn_classifier.fit_one_cycle(5, 2e-2, moms=(0.8,0.7))
learn_classifier.recorder.plot_losses(return_fig=True)
learn_classifier.recorder.plot_metrics(return_fig=True)

# Tune a little more
learn_classifier.fit_one_cycle(5, slice(1e-2/(2.6**4),1e-2), moms=(0.8,0.7))
learn_classifier.recorder.plot_losses(return_fig=True)
learn_classifier.recorder.plot_metrics(return_fig=True)


learn_classifier.save_encoder('wiki-sentiment-test-data')
learn_classifier.export('trained_model.pkl')
print("DONE")

#--------------------------------------------------------------

'''
"""Parte Final, parte de colocar os valores"""
#this function accesses all of the monthly files and analyses them (it's the last thing to run)R
local = "/content/drive/My Drive/nlp/coleta/top-processed/"
os.chdir(local) #change current directory

for directory in os.listdir():
  os.chdir(directory)
  print('working on files from: ', directory)
  for file in os.listdir():	#get all files from this directory
    if file.endswith(".npy"):
      path = os.getcwd()+ '/'+ file
      #print('\t',file)

      tweets_df = np.load(path, allow_pickle=True).item()
      df = pd.DataFrame.from_dict(tweets_df, orient='index')
      #print(df.columns)

      #eh importante lembrar se a hashtag eh a favor ou contra as armas. Uma hashtag considerada a favor (2nd) vai ser positivo para armas e negativo para contrrole
      #ja uma hashtag considerada contra (March...) vai ser positivo para controle e neg para armas
      # ARRUMAR ISSO DEPOIS (VAI TER Q SER FEITO "MANUALMENTE")
      
      df.assign(fastai=np.nan)#, flair=np.nan) #adding columns for textblob

      for index, row in df.iterrows():
          #fastai
          i = 0
        #score = analyzer.polarity_scores(row['text'])
        #print("{:-<40} {}".format(row['text'], str(score)))
      dicio = df.to_dict(orient='index') #saving process
      saving_path = os.getcwd()+'/'+'final/'+file
      np.save(saving_path, dicio)
      #print(df.head(20))
    #break;
  #break;		
  os.chdir('..') #get back

  '''
