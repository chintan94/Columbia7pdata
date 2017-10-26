import pandas as pd
import spacy
from collections import Counter, defaultdict

def token_without_last2(a):
    b=[]
    for i in a:
        sample = i.split()
        nsam = sample[0:-2]
        nstring = ' '.join(nsam)
        b.append(nstring)
    return b

def freqCount(f,threshold=100): #doc is the file name, threshold is the level of frequency
    dtypes = {"transaction_key" : "int64", 
              "accountholder_fi_key": "int64",
              "accountholder_key" : "int64",
              "account_key" : "int64",
              "accountholder_zip" : "int64",
              "accountholder_zip_post" : "float64",
              "accountholder_birth_year": "int64",
              "accountholder_gender" : object,
              "account_type" : object,
              "transaction_description" : object,
              "transaction_swipe_date" : "datetime64",
              "transaction_settlement_date" : "datetime64",
              "transaction_amount_in_cents" : "int64",
              "in_userpanel" : object,
              "valid_merchant_transactions" : object,
              "valid_merchant_transactions_2" : object,
              "ticker" : object,
              "cleansed_name" : object}

    columns = ["transaction_key", 
              "accountholder_fi_key",
              "accountholder_key",
              "account_key" ,
              "accountholder_zip",
              "accountholder_zip_post",
              "accountholder_birth_year",
              "accountholder_gender",
              "account_type",
              "transaction_description",
              "transaction_swipe_date",
              "transaction_settlement_date",
              "transaction_amount_in_cents",
              "in_userpanel",
              "valid_merchant_transactions",
              "valid_merchant_transactions_2",
              "ticker",
              "cleansed_name"]

    df = pd.read_csv(f, sep="\t", nrows=10000, dtype = dtypes)
    df.columns = columns 
    a=df.iloc[:,9]
    b = token_without_last2(a)
    
    nlp = spacy.load('en')
    frequency = Counter()
    for i in b:
        doc = nlp(i.decode('utf8'))
        for j in doc.ents:
            frequency[j.lemma_] += 1
    
    return dict((k,frequency[k]) for k in frequency.keys() if frequency[k] > threshold)
    
def mergeDic(a,b):
    c = Counter(a)
    d = Counter(b)
    dic = c+d
    return dic
