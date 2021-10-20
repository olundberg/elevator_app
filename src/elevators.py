"""Dash modules for time elevators plot"""
import numpy as np
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=1, subplot_titles=("Elevators",))
y = [0 for val in range(5)]
x = [val for val in range(5)]
fig.add_trace(go.Scatter(x=x, y=y,
                         mode="markers",
                         marker_symbol="square",
                         marker_size=75),
              row=1, col=1)
fig.update_yaxes(title_text="Level", row=1, col=1)
fig.update_xaxes(title_text="Elevator", row=1, col=1)
fig.update_layout(yaxis_range=[-1, 20])
fig.update_layout(
        template="plotly_white",
        xaxis={"type": 'category'},
        transition={
                'duration': 500,
                'easing': 'cubic-in-out'
        },)
style = {"width": "95.9%", "margin-left": "2%", "height": "90vh"}


def get_elevator(figa=None, n_elevators=5, n_levels=20):
    """Convenience function

    :param figa:
    :param n_elevators: Number of elevators
    :param n_levels: Number of levels
    :returns :
    """
    elevators = [0 for _ in range(n_elevators)]
    opts = [{"label": val, "value": val} for val in range(n_levels)]

    dropdown = dcc.Dropdown(value=0,
                            id="elevator_level",
                            options=opts,
                            clearable=False)

    #content = html.Div([dropdown,
    #                    dcc.Graph(figure=fig, id="elevator_fig", style=style),
    #                   ])
    content = html.Div([dropdown,
                        dcc.Graph(id="elevator_fig", style=style),
                       ])

    return content

def update_elevator(elevators):
    return {
        'data': [{
            'x': [
                1,2,3,4,5
            ],
            'y': elevators,
            'type': 'scatter',
            'mode': 'markers',
            'marker': {'size': 50,
                       'symbol': "square"
            }
        }],
        'layout': {"height": "90vh",
            # You need to supply the axes ranges for smooth animations
            'xaxis': {'range': [0, 6]},
            'yaxis': {'range': [-1, 20]},
            'transition': {'duration': 2000,
                           'easing': 'cubic-in-out'
            }
        }
    }
