import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


def initialization (df, stock, start_date ,end_date):
    """this function takes a dataframe and does initial steps (the dataframe should be in datetimeformat of yyyy-mm-dd)

    Args:
        df (DataFrame): the dataFrame that is to be initialized
        stock (string): the stock that is to be selected
        start_date (datetime): the start date of the stock
        end_date (datetime): the end date of the stock
    """

    #changing into datetime format of pandas
    df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

    #selecting the stock with its start date and end date
    req_stock_df= df[(df['Date'] > start_date ) & (df['Date'] < end_date ) & (df['Symbol']==stock )]


    req_stock_df = req_stock_df.sort_values('Date')

    return req_stock_df


def plotly_plot_line(df,x_col,y_col,stock):
    
    

    fig = px.line(df, x = df[x_col],y =df[y_col], title = f'{y_col} of the given dates of {stock}')
    fig.update_layout(
    width=1000,  
    height=400
    )

    fig.show()

def remove_average_outliers(df): 
    df=df[(df['Average']>df['Low']) & (df['Average']<df['High'])]
    return df





