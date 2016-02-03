# -*- coding: utf-8 -*-

"""
octogrid.publisher.publisher

This module helps with publishing the graph network using Plotly
"""

import string
import igraph as ig
from random import choice
import plotly.plotly as plotly
from plotly.graph_objs import *
from os.path import join, expanduser, isfile
from ..generator.generator import generate_network
from ..utils.utils import username_to_file, community_colors, login_as_bot


def prepare_plot_data(data_file):
    """
    Return a list of Plotly elements representing the network graph
    """

    G = ig.Graph.Read_GML(data_file)

    layout = G.layout('graphopt')
    labels = list(G.vs['label'])

    N = len(labels)
    E = [e.tuple for e in G.es]

    community = G.community_multilevel().membership
    communities = len(set(community))

    color_list = community_colors(communities)

    Xn = [layout[k][0] for k in range(N)]
    Yn = [layout[k][1] for k in range(N)]

    Xe = []
    Ye = []

    for e in E:
        Xe += [layout[e[0]][0], layout[e[1]][0], None]
        Ye += [layout[e[0]][1], layout[e[1]][1], None]

    lines = Scatter(x=Xe,
                    y=Ye,
                    mode='lines',
                    line=Line(color='rgb(210,210,210)', width=1),
                    hoverinfo='none'
                    )
    plot_data = [lines]

    node_x = [[] for i in range(communities)]
    node_y = [[] for i in range(communities)]
    node_labels = [[] for i in range(communities)]

    for j in range(len(community)):
        index = community[j]

        node_x[index].append(layout[j][0])
        node_y[index].append(layout[j][1])
        node_labels[index].append(labels[j])

    for i in range(communities):
        trace = Scatter(x=node_x[i],
                        y=node_y[i],
                        mode='markers',
                        name='ntw',
                        marker=Marker(symbol='dot',
                                      size=5,
                                      color=color_list[i],
                                      line=Line(
                                          color='rgb(50,50,50)', width=0.5)
                                      ),
                        text=node_labels[i],
                        hoverinfo='text'
                        )

        plot_data.append(trace)

    return plot_data


def publish_network(user=None, reset=False):
    """
    Generate graph network for a user and plot it using Plotly
    """

    username = generate_network(user, reset)
    network_file = username_to_file(username)

    plot_data = prepare_plot_data(network_file)
    data = Data(plot_data)

    # hide axis line, grid, ticklabels and title
    axis = dict(showline=False,
                zeroline=False,
                showgrid=False,
                showticklabels=False,
                title=''
                )

    width = 800
    height = 800

    layout = Layout(title='GitHub Network for "{0}"'.format(username),
                    font=Font(size=12),
                    showlegend=False,
                    autosize=False,
                    width=width,
                    height=height,
                    xaxis=XAxis(axis),
                    yaxis=YAxis(axis),
                    margin=Margin(
                        l=40,
                        r=40,
                        b=85,
                        t=100,
                    ),
                    hovermode='closest',
                    annotations=Annotations([
                        Annotation(
                            showarrow=False,
                            text='This igraph.Graph has the graphopt layout',
                            xref='paper',
                            yref='paper',
                            x=0,
                            y=-0.1,
                            xanchor='left',
                            yanchor='bottom',
                            font=Font(
                                size=14
                            )
                        )
                    ]),
                    )

    fig = Figure(data=data, layout=layout)

    # use credentials of the bot "octogrid", if user isn't authenticated
    login_as_bot()

    try:
        plot_id = ''.join(choice(string.lowercase) for i in range(5))
        plot_url = plotly.plot(
            fig, filename='Octogrid: GitHub communities for {0} [v{1}]'.format(username, plot_id))

        print 'Published the network graph at {0}'.format(plot_url)
    except Exception, e:
        raise e
