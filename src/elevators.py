"""Dash modules for time elevators plot"""
from dash import dcc
from dash import html
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=1, subplot_titles=("Elevators",))
style = {"width": "95.9%", "margin-left": "2%", "height": "90vh"}


def get_elevator(n_elevators=5, n_levels=20):
    """Convenience function

    :param n_elevators: Number of elevators
    :param n_levels: Number of levels
    :returns :
    """
    opts = [{"label": val, "value": val} for val in range(n_levels)]

    dropdown_lvl = dcc.Dropdown(value=0,
                                id="elevator_level",
                                options=opts,
                                clearable=False)

    content = html.Div([html.Div("Choose level:"), dropdown_lvl,
                        dcc.Graph(id="elevator_fig", style=style),
                        ])

    return content


def update_elevator(elevators, transition_time):
    """

    :param elevators:
    :param time:
    :returns :
    """
    elevator_pos = [val for val in range(1, len(elevators)+1)]

    return {'data': [{'x': elevator_pos, 'y': elevators,
                      'type': 'scatter', 'mode': 'markers',
                      'marker': {'size': 50, 'symbol': "square"}
                      }],
            'layout': {"height": "90vh", "title": "Elevators",
                       'xaxis': {"title": "Elevator no.", 'range': [0, 6],
                                 },
                       'yaxis': {"title": "Level", 'range': [-1, 20]},
                       'transition': {'duration': transition_time,
                                      'easing': 'cubic-in-out'}
                       }
            }
