"""Main for gvirus application"""
import os
import json
import dash
import dash_bootstrap_components as dbc
from dash import  dcc
from dash import html
from dash.dependencies import Input, State, Output, ALL, MATCH
from dash.exceptions import PreventUpdate
from src.elevators import get_elevator
import traceback
import platform
from src.elevator_algo import elevator_algo
from src.elevators import update_elevator

__AUTHOR__ = "Oscar Lundberg"

EXTERNAL_STYLESHEETS = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
app = dash.Dash(external_stylesheets=[dbc.themes.PULSE])

app.layout = html.Div([get_elevator()])
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True


@app.callback(Output("elevator_fig", "figure"),
              Input("elevator_level", "value"),
              State("elevator_fig", "figure"))
def input_value_cb(elevator_value: int, elevators):
    """Change input value from edit field above sliders
    :returns value: The new value set
    """
    # Calculate new state for elevators
    try:
        current_state = elevators["data"][0]["y"]
    except:
        current_state = [0, 0, 0, 0, 0]
    elevators_new = elevator_algo(elevator_value,
                                  current_state)

    return update_elevator(elevators_new)



server = app.server

if __name__ == '__main__':
    PORT = 5000  # 3
    if platform.system() == "Linux":
        app.run_server(host="0.0.0.0", debug=True, port=PORT)
    else:
        PORT = 8083
        app.run_server(debug=False, dev_tools_ui=False,
                       dev_tools_props_check=False)
