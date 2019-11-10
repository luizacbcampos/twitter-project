import vaderSentiment as vader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
import os

local = "coleta/top-processed/"

os.chdir(local) #change current directory

for directory in os.listdir():
	os.chdir(directory)
	print('working on files from: ', directory)
	for file in os.listdir():	#get all files from this directory
		if file.endswith(".npy"):
			path = os.getcwd()+ '/'+ file

			print('\t',file)

			tweets_df = np.load(path, allow_pickle=True).item()

			#print(tweets_df)
			
			df = pd.DataFrame.from_dict(tweets_df, orient='index')
			#print(df.columns)



			#É importante lembrar se a hashtag é a favor ou contra as armas. Uma hashtag considerada a favor (2nd) vai ser positivo para armas e negativo para contrrole
			#já uma hashtag considerada contra (March...) vai ser positivo para controle e neg para armas
			# ARRUMAR ISSO DEPOIS (VAI TER Q SER FEITO "MANUALMENTE")
			#vader goes from [-1,1]
			analyzer = SentimentIntensityAnalyzer()
			df.assign(vader_neg=np.nan,vader_neu=np.nan, vader_pos=np.nan, vader_compound=np.nan) #adding the new columns

			for index, row in df.iterrows():
				score = analyzer.polarity_scores(row['text'])
				df.at[index,'vader_neg'] = score['neg']
				df.at[index,'vader_neu'] = score['neu'] 
				df.at[index,'vader_pos'] = score['pos']
				df.at[index,'vader_compound'] = score['compound']
				#print("{:-<40} {}".format(row['text'], str(score)))

			dicio = df.to_dict(orient='index') #saving process
			saving_path = os.getcwd()+'/'+'vader/'+file
			np.save(saving_path, dicio)
				
	os.chdir('..') #get back