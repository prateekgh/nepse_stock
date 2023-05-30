import function_initial as fn
import pandas as pd
import numpy as np 




def export_time_average_prices(df,stock,start_date,end_date):
    df = fn.initialization(df,stock,start_date,end_date)

    df['LTP'] = df['LTP'].str.replace(',', '')  # Remove commas from the values
    df['LTP'] = pd.to_numeric(df['LTP'])
    df['High'] = df['High'].str.replace(',', '')  # Remove commas from the values   
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = df['Low'].str.replace(',', '')  # Remove commas from the values
    df['Low'] = pd.to_numeric(df['Low'])
    df['Open'] = df['Open'].str.replace(',', '')  # Remove commas from the values
    df['Open'] = pd.to_numeric(df['Open'])
    df['Turnover'] = df['Turnover'].str.replace(',', '')  # Remove commas from the values
    df['Turnover'] = pd.to_numeric(df['Turnover'])
    df['Quantity'] = df['Quantity'].str.replace(',', '')  # Remove commas from the values
    df['Quantity'] = pd.to_numeric(df['Quantity'])


    df['Average']= pd.Series(df['Turnover']/df['Quantity']) #adding average column and calculating it 

    df = fn.remove_average_outliers(df)  #function to remove outliers from average

    df = df[['Average']].copy()

    df =df.reset_index()
    df.drop('index' , axis=1 , inplace = True)


    return(df)



    
