# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 01:36:01 2022

@author: Mahi
"""
import pandas as pd

#read = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv' , sep=';')

#summary of the data
data.info()

# working with calculations

# defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemPurchased = 6


# Mathematical operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = ProfitPerItem * NumberOfItemPurchased

CostPerTransaction = NumberOfItemPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemPurchased * SellingPricePerItem


#CostPerTransaction column calulation

#CostPerTransaction =  CostPerItem * NumberOfItemPurchased
#variable = dataframe['columnName']

CostPerItem = data['CostPerItem']
NumberOfItemPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = NumberOfItemPurchased * CostPerItem

#adding this column into a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#SellingPricePerTransaction calulation 
#SellingPricePerItem = data['SellingPricePerItem']

data['SellingPricePerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


#Profit calculation

#profit = sales - cost

data['ProfitPerTransaction'] = data['SellingPricePerTransaction'] - data['CostPerTransaction']

#markup = (sales - cost)/ cost
data['Markup'] = (data['SellingPricePerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

# markup = Profit/ cost

data['Markup'] = data['ProfitPerTransaction']  / data['CostPerTransaction']


RoundMarkup = round(data['Markup'],2)
data['Markup'] =  round(data['Markup'],2) 

#combining data fields

my_date = "Date"+"-"+"Month"+"-"+"Year"

print(data['Day'].dtype)

day = data['Day'].astype(str) 

print(day.dtype)
year = data['Year'].astype(str)

my_date = day+"-"+data['Month']+"-"+ year

data['date']= my_date

#using iloc to view specific rows and columns 
data.iloc[0]
data.iloc[0:3] # to view first three rows
data.iloc[-5:] #last five rows
data.iloc[:,2] # all rows on column 2 

# use split function to split the clientkeywords column
split_col = data['ClientKeywords'].str.split(',', expand = True)

data['ClientAge']= split_col[0]
data['ClientType']= split_col[1]
data['lengthOfContract']= split_col[2]

#using replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['lengthOfContract'] = data['lengthOfContract'].str.replace(']','')

#using lower function to change item  to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing a new dataset

season = pd.read_csv('value_inc_seasons.csv', sep =';')
season.head()

#mege_files : mege.df = pd.merge(df_old, df_new , on= 'key)
data = pd.merge(data,season , on = 'Month')

#drop columns 
#df = df.drop('columnname' , axis = 1)
data = data.drop(['ClientKeywords','Year','Month', 'Day'], axis = 1 )

#export in CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)




































