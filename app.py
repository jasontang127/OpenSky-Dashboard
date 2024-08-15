from dash import Dash, html, dcc, callback, Input, Output, State
import numpy as np
import pandas as pd
import datetime as dt
import time
import json
import requests
from opensky_api import OpenSkyApi
# import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

login_info = {
    'username':'',
    'password':''
}

state_keys = ['icao24','callsign','origin_country',
              'time_position','last_contact','longitude',
              'latitude','geo_altitude','on_ground',
              'velocity','true_track','vertical_rate',
              'sensors','baro_altitude','squawk',
              'position_source','category']

api = OpenSkyApi(username=login_info['username'], password=login_info['password'])

# read and clean dataframe
flights_df = pd.read_pickle('flights.pkl')
flights_df[state_keys] = pd.DataFrame(flights_df.states.tolist(), index=flights_df.index)
flights_df['time'] = flights_df['time'].apply(lambda x: dt.datetime.fromtimestamp(x))
flights_df['origin_country'] = flights_df['origin_country'].str.strip(' \n')
flights_df['numflights'] = flights_df['states'].apply(lambda x: len(x))

# TODO: callback for datetime range

# set up graphs
def make_line_chart(df):
    return px.line(df.groupby('time', as_index=False).count(), x='time', y='states')

# line_chart = px.line(flights_df.groupby('time', as_index=False).count(), x='time',y='states')
# line_chart = sns.lineplot(data=flights_df.groupby('time', as_index=False).count(), x='time',y='states')

def make_pie_chart(df):
    return px.pie(df.groupby('origin_country', as_index=False).count()[['origin_country','numflights']].sort_values(by='numflights',ascending=False).head(5), values='numflights', color='origin_country', names='origin_country')
# pie_chart = px.pie(flights_df.groupby('origin_country', as_index=False).count()[['origin_country','numflights']].sort_values(by='numflights',ascending=False).head(5), values='numflights', color='origin_country', names='origin_country')

# dash layout
app = Dash()

app.layout = html.Div(
    children = [
        html.H1(children='OpenSky Flights Graphs'),

        html.Div(children=[
            dcc.Input(id='start_date',type='text'),
            dcc.Input(id='end_date',type='text'),
            html.Button(id='submit_date', n_clicks = 0, children='Submit')]),

        dcc.Graph(
            id='line_graph',
            figure = make_line_chart(flights_df)
        ),
        
        dcc.Graph(
            id='pie_chart',
            figure = make_pie_chart(flights_df)
        )
    ]
)

@callback(Output('line_graph','figure'),
          Output('pie_chart','figure'),
          Input('submit_date', 'n_clicks'),
          State('start_date','value'),
          State('end_date','value'),
          prevent_initial_call=True)
def filter_date(n_clicks, start_date, end_date):
    start = dt.datetime.fromtimestamp(int(start_date))
    end = dt.datetime.fromtimestamp(int(end_date))
    df = flights_df[(flights_df['time'] >= start) & (flights_df['time'] <= end)]
    return make_line_chart(df), make_pie_chart(df)
    # convert start_date/end_date from epoch to normal datetime
    # create new df
    # create graphs based on new df
    # return

app.run(debug=False)