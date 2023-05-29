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


def plotly_plot_line(df):


    x_values = df['Date']
    y_values=df['LTP']
    
# Create the line plot
    fig = go.Figure(data=go.Scatter(x=x_values, y=y_values, mode='lines'))

# Invert the y-axis
    fig.update_yaxes(autorange='reversed')

# Customize the plot (optional)
    fig.update_layout(title="Line Plot Example", xaxis_title="X-axis", yaxis_title="Y-axis")

# Display the plot
    fig.show()







    #fig.update_xaxes(autorange='reversed')

    # Flip the y-axis
    #fig.update_yaxes(autorange='reversed')




def mat_plot_line(df):
    fig,ax = plt.subplots()

    ax.plot(df['Date'],df['LTP'])
    ax.set_xlabel('Date')
    ax.set_ylabel('LTP')
    ax.invert_yaxis()

    plt.grid(True)
    plt.show()









