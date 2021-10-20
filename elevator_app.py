"""Main for gvirus application"""
import dash
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, State, Output
from src.elevators import get_elevator
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

    :param elevator_value:
    :param elevators:
    :returns value: The new value set
    """
    # Calculate new state for elevators

    # Startup will fail
    try:
        current_state = elevators["data"][0]["y"]
    except Exception as e:
        print(e)
        current_state = [0, 0, 0, 0, 0]

    elevators_new, lvl_diff = elevator_algo(elevator_value,
                                            current_state)

    fig = update_elevator(elevators_new, lvl_diff*1000*2)

    return fig


server = app.server

if __name__ == '__main__':
    PORT = 5000  # 3
    if platform.system() == "Linux":
        app.run_server(host="0.0.0.0", debug=True, port=PORT)
    else:
        PORT = 8083
        app.run_server(debug=False, dev_tools_ui=False,
                       dev_tools_props_check=False)
