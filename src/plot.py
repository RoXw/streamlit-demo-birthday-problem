import imp
import plotly.graph_objects as go
import numpy as np
from src.birthdayProblem import birthday_paradox, birthday_problem

def default_birthday_problem_plot(z: list):
    """Create a plotly line plot with probability on y-axis and
    with number of individuals on x-axis for various 
    number of days (sample space) provided in z

    Args:
        z (list): number of days (sample space) in a year
    """
    fig = go.Figure()
    for day in z:
        x = [int(xi) for xi in np.geomspace(1, day, num=11)]
        y = [birthday_problem(day, xi) for xi in x]
        # plot line
        fig.add_trace(go.Scatter(x=x, y=y, name=f"day: {day}",
                    line_shape='spline'))
    fig.update_traces(mode='lines+markers')
    fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
    fig.update_layout(title=f'Probability of atleast two individuals having same birthday in a sample space',
                        xaxis_title='Number of individuals',
                        yaxis_title='Probability (%)')
    return fig


def default_birthday_paradox_plot(z: list):
    """Creates default birthday paradox plot

    Args:
        z (list): number of days (sample space) in a year
    """
    fig = go.Figure()
    y = [birthday_paradox(day) for day in z]
    y2 = [int(np.sqrt(day)) for day in z]
    fig.add_trace(go.Scatter(x=z, y=y, name=f"50% prob",
                    line_shape='spline'))
    fig.add_trace(go.Scatter(x=z, y=y2, name=f"Square root",
                    line_shape='spline'))
    fig.update_traces(mode='lines+markers')
    fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
    fig.update_layout(title=f'Minimum number of individuals required for 50% probability in birthday problem',
                        xaxis_title='Number of days (sample space)',
                        yaxis_title='Number of individuals')
    return fig


def birthday_problem_plot(day: int):
    """For a given sample space plot how the prob increases 
    with increase in individuals

    Args:
        day (int): number of days (sample space)
    """
    x = [int(xi) for xi in np.geomspace(1, day, num=11)]
    y = [birthday_problem(day, xi) for xi in x]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y,
                    line_shape='spline'))
    fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))
    fig.update_layout(title=f'Probability of atleast two individuals having same birthday in a year with days: {day}',
                        xaxis_title='Number of individuals',
                        yaxis_title='Probability (%)')
    return fig

