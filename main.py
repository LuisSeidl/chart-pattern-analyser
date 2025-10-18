import pandas as pd
import datetime as dt
import pandas_datareader.data as web
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
from dbclient import DatabaseClient
from financial_data import EurUsd_Daily
from datetime import datetime

db_url = 'postgresql+psycopg2://postgres:postgres@localhost/financial_data'
dbclient = DatabaseClient(db_url)


data = dbclient.get_query_as_dataframe("SELECT * FROM eur_usd_daily WHERE date > 2020-01-01")

