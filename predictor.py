import numpy as np
import pandas as pd 
import pickle
import os 
from nltk.stem.snowball import SnowballStemmer


class Predictions():
    '''class to make the predictions given the model and then 
    append the query to the data set that you currently have '''
    def __init__(self,model,data_path):
        self.model = model
        self.path = data_path
        self.data = pd.read_csv(data_path)
        self.stemmer = SnowballStemmer('english')
        punctuation='["\'?,\.]'
        self.abbr_dict = {
            "what's":"what is",
            "what're":"what are",
            "where's":"where is",
            "where're":"where are",
            "i'm":"i am",
            "we're":"we are",
            "it's":"it is",
            "that's":"that is",
            "there's":"there is",
            "there're":"there are",
            "i've":"i have",
            "who've":"who have",
            "would've":"would have",
            "not've":"not have",
            "i'll":"i will",
            "it'll":"it will",
            "isn't":"is not",
            "wasn't":"was not",
            "aren't":"are not",
            "weren't":"were not",
            "can't":"can not",
            "couldn't":"could not",
            "don't":"do not",
            "didn't":"did not",
            "shouldn't":"should not",
            "wouldn't":"would not",
            "doesn't":"does not",
            "haven't":"have not",
            "hasn't":"has not",
            "hadn't":"had not",
            "won't":"will not",
            punctuation:'',
            '\s+':' ', # replace multi space with one single space
        }
    def process_query(self,query):
        
        '''Returns a processed and stemmed query'''
        query = query.lower()
        res = ''
        for k in query.split():
            if k in self.abbr_dict:
                res+=' ' + self.abbr_dict[k]
            else:
                res+=' ' + k 
        
        res = ' '.join([self.stemmer.stem(y) for y in res.split()])
        return res 
    
    def append_query(self,query,ailment):
        '''Take the query and prediction and then append it to original data '''
        
        col1 = 'stemmed_phrase'
        col2 = 'Prompt'
        self.data = self.data.append([{col1 : query[1:-1] , col2 : ailment}] , ignore_index = True)
        try: 
            self.data = self.data.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)
        except:
            pass
        try:
            self.data = self.data.drop(['Unnamed: 0'],axis=1)
        except:
            pass
        self.data.to_csv(self.path)
        