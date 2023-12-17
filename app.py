import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

datasets_public = [
    {'label': '21K Nether (2019)', 'value': '21k_nether.csv'},
    {'label': '21K End (2019)', 'value': '21k_end.csv'},
    {'label': '20K Overworld (2017)', 'value': '20k_overworld.csv'},
]

app.layout = html.Div(id="parentdiv", children=[
    html.Div(children=[
        html.Div(dcc.RadioItems(id='dflist', options=datasets_public, value='20k_overworld.csv')),
        html.Div([dcc.Graph(id='scatter-plot')])])])


@app.callback(
    Output("scatter-plot", "figure"),
    Input("dflist", "value"))
def update_bar_chart(dflist):
    df = pd.read_csv("data/" + dflist)
    df = df.fillna("")
    fig = px.scatter(df, x="x", y="z", hover_data=['x', 'y', 'z', 'line'])
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
