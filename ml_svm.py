'''
Created on 2014/7/15

@author: Alison, Y.Y Wang
'''
### Required packages
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn import svm
from operator import itemgetter
import numpy as np
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
import nltk
import csv

""" Initial Parameter Setting"""
marklist =['?','!',',','.']


def cleanmark(listOfText,mark):
    for i in range(len(listOfText)):
        listOfText[i] = listOfText[i].strip(mark)
    return listOfText

def extractLabelandDataFromTXT(txtFile):
    openedFile = open(txtFile,'r')
    content=[]
    label=[]
    for record in openedFile.readlines():

        category, rawtext = record.split(',',1)
        label.append(category)
        content.append(rawtext)
    return label,content

def openAndCleanTest(txtFile):
    raw=open(txtFile,'r')
    idlist=[]
    textlist=[]
    rows = []
    for record in raw.readlines():
        rows.append(record.split('\t'))
    for r in rows:
        idlist.append(r[0])
        text=""
        for i in range(1,len(r)):
            if r[i] != '' and r[i] !='\n':
                text += (r[i])
        textlist.append(text)
    return idlist,textlist

def stem_tokens(tokens):
    stemmer = nltk.PorterStemmer()
    stemmedTokens = []
    for item in tokens:
        stemmedTokens.append(stemmer.stem(item))
    return stemmedTokens

def myTokenizer(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens)
    return stems


# import train data
train_label, train_data = extractLabelandDataFromTXT("train.txt")

# import test data
test_id, test_data = openAndCleanTest("testtxt.txt")

# Vectorize the data
vectorizer = TfidfVectorizer(ngram_range=(1,2),
                             stop_words='english',
                             tokenizer=myTokenizer,  # Input is tokenized
                             norm='l2',
                             decode_error='ignore')

X_train =vectorizer.fit_transform(train_data)
X_test = vectorizer.transform(test_data)


# Feature selection using chi2
ch2 = SelectPercentile(chi2,percentile=50)
selected_Xtrain = ch2.fit_transform(X_train,train_label)
selected_Xtest = ch2.transform(X_test)


## Classify the data using feature selection
selected_clf= LinearSVC().fit(selected_Xtrain, train_label)
selected_clf_predict = selected_clf.predict(selected_Xtest)


## Write result into CSV file

result = zip(test_id,selected_clf_predict)
print len(result)
print result[0]


with open("linearSVC_selector50.csv",'wb') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(['Id','Category'])
    for row in result:
        csvwriter.writerow(row)

