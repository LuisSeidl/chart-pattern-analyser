import pandas as pd
import datetime as dt
import pandas_datareader.data as web
from dash import Dash, html, dcc, callback, Output, Input, dash_table
import plotly.express as px

ticker = 'AAPL'
data = web.DataReader('ticker','stooq', start='2015-01-01', end='2025-01-01')

app = Dash()

app.layout = [html.Div(children=f'Displaying the OHLC for {ticker}'),
              dcc.Graph(figure=px.line(data_frame=data))
              ]


if __name__ == '__main__':
    app.run(debug=True)