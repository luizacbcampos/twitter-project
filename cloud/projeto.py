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

# ----------------------------------------------------------------------------------------------------------------------
#test stuff and etc

"""# Loading into fast ai"""

#data = (TextList.from_df(sent_140_train, cols='text').split_by_rand_pct(0.2).label_for_lm().databunch(bs=48))
#or just load
data = load_data(path='',file='sentiment-train-data.pkl', bs=48) #data.load(path, 'sentiment-train-data.pkl')
#data.show_batch()


#saving the data bunch
#data.save('only-sentiment-train-data.pkl')
#print("saved picle")
#----------------------------------------------------------------------------------------------------------------------
"""### Fit the deep learning model with domain specific data"""
'''
learn = language_model_learner(data,AWD_LSTM, drop_mult=0.3)

# select the appropriate learning rate
learn.lr_find()

# we typically find the point where the slope is steepest
learn.recorder.plot()

# Fit the model based on selected learning rate
learn.fit_one_cycle(5, 1e-2, moms=(0.8,0.7))

# Tune a little more
learn.unfreeze()
learn.fit_one_cycle(5, 1e-3, moms=(0.8,0.7))

# Save the encoder for use in classification
learn.save_encoder('sentiment-train-data.pth')
'''
#-----------------------------------------------------------------------------------
#PARTE DA WIKi

print("wiki part")
#aqui eu coloco o modelo da wikipedia preh-treinado tb
perplexity = Perplexity()
learn = language_model_learner(data, AWD_LSTM, drop_mult=0.3, 
                               pretrained=True, pretrained_fnames = ['wiki_model_10epochs','wiki_vocab_10epochs'],
                               metrics=[accuracy, perplexity]).to_fp16()
print("here")
learn.lr_find()

learn.recorder.plot()

learn.fit_one_cycle(5, 1e-2, moms=(0.8,0.7))

learn.fit_one_cycle(5, 1e-3, moms=(0.8,0.7))

# Save the encoder for use in classification
learn.save_encoder('wiki-train-data')








'''
"""Parte Final, parte de colocar os valores"""

#this function accesses all of the monthly files and analyses them (it's the last thing to run)
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
