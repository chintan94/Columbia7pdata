# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:07:01 2017

@author: cd2966
"""

import pandas as pd

#Input Definition 
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

df = pd.read_csv("201601.tsv", sep="\t", nrows=100000, dtype = dtypes)
df.columns = columns 