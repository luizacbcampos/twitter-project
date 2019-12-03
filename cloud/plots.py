import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
import os
import re

def save(df,file):
	dicio = df.to_dict(orient='index') #saving process
	saving_path = os.getcwd()+'/'+'vader/'+file
	np.save(saving_path, dicio)

def gera_csv():
    local = "coleta/"
    os.chdir(local) #change current directory
    month = []
    counts = []
    tags = []
    for directory in os.listdir():
        os.chdir(directory)
        os.chdir('vader/final/') #acessa o diretorio vader
        print('working on files from: ', directory)
        dfs = []
        for file in os.listdir():	#get all files from this directory
            if file.endswith(".npy"):
                path = os.getcwd()+ '/'+ file
                tweets_df = np.load(path, allow_pickle=True).item()
                df = pd.DataFrame.from_dict(tweets_df, orient='index')
                df['file'] = file[:-11]
                dfs.append(df)
                path = path[:-4] + '.csv'
                
                df.reset_index().to_csv(path, sep='\t', index=False)
                #break;
    	#break;
        if(len(dfs) > 0):
            combined = pd.concat([df for df in dfs])
            combined = combined.drop(columns=['hashtags','text','datetime','is_reply', 'is_retweet','nbr_favorite', 'nbr_reply', 'user_id',
       			'usermentions', 'usernameTweet'])
            combined = combined.drop(columns=['vader_pos', 'vader_neg', 'vader_neu'])
            combined['fastai'] =  minmax_scale(combined['wiki'].astype(int), feature_range=(-1,1))
            combined = combined.drop(columns=['wiki'])
            combined  = combined.reset_index(drop=True)
            combined['month'] = directory
            month.append(combined)

        os.chdir('../../..') #get back
    todos = pd.concat([df for df in month])
    #print(todos.head())
    General = ['2nd','firearms','guns','second_am']
    Control = ['gunsense','gunsensepatriot','votegunsense','guncontrolnow','momsdemandaction','momsdemand','demandaplan','nowaynra','gunskillpeople','gunviolence','endgunviolence','NeverAgain','MarchForOurLives']
    Rights = ['gunrights','protect2a','molonlabe','molonlab','noguncontrol','progun','nogunregistry','votegunrights','firearmrights','gungrab','gunfriendly']
    for index, row in df.iterrows():
        if string in General:
            df.at[index,'file'] = 'General'
        elif string in Rights:
            df.at[index,'file'] = 'Rights'
        else:
            df.at[index,'file'] = 'Control'
    ano = todos.groupby(['file']).mean()
    print(ano.head())
    ano.plot.bar(rot=0)
    title = "Comparação das análises para todo o período analisado"
    plt.xticks(fontsize=8, rotation=80)
    plt.xlabel('hashtags')
    plt.tight_layout()
    plt.title(title)
    imagem = 'ano2.png'
    plt.savefig(imagem, bbox_inches='tight')
    plt.show()

        #df = pd.read_csv('dados-gerais.csv')
	

def gera_csv_mensal():
    local = "coleta/"
    os.chdir(local) #change current directory
  
    for directory in os.listdir():
        os.chdir(directory)
        os.chdir('vader/final/') #acessa o diretorio vader
        files = []
        print('working on files from: ', directory)
        for file in os.listdir():       #get all files from this directory
            if file.endswith(".npy"):
                path = os.getcwd()+ '/'+ file
                print('\t',file)
                files.append(file)
                #break;
        #break;
        name = directory+'.csv'
        combined_csv=pd.concat([pd.read_csv(f, sep='\t', index_col=0, encoding='latin-1') for f in files])
        combined_csv.to_csv(name, index=False)
        os.chdir('../../..') #get back
        #df = pd.read_csv('dados-gerais.csv')

gera_csv()
#gera_csv_mensal()
#vader_analysis()
#get_monthly_mean()
#csv_grande()
#plot_por_mes()
#plot_bonitinho()

#df = pd.read_csv('dados-gerais.csv')
#print(df.counts.sum())
#df = pd.read_csv('coleta/top-processed/10-2018/vader/data.csv')
#print(df.columns)

#scale the results
#audio_scaled =  sklearn.preprocessing.minmax_scale(audio, feature_range=(-1,1))



#df.vader_compound = pd.to_numeric(df.vader_compound,errors='coerce')
#df = df.drop(df[(df.textblob >= -1) & (df.textblob <= 1)].index)
#df = df.drop(df[(df.vader_compound >= -1) & (df.vader_compound <= 1)].index)
