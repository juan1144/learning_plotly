from django.shortcuts import render
import plotly.graph_objects as go
from plotly.io import to_html

def index(request):
    return render(request, 'dashboards/index.html')



def card1(request):
    labels = ["A", "B", "C", "E", "G", "N"]
    values = [120, 90, 150, 75, 120, 165]

    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=values,
            marker=dict(
                color='rgb(142, 22, 22,0.8)',
                # color=[ # Custom BG Color per bar in chart
                #     'rgba(255, 99, 132, 1.0)',
                #     'rgba(54, 162, 235, 1.0)',
                #     'rgba(255, 206, 86, 1.0)'
                # ],
                line=dict(color=[ # Custom Line Color per bar in chart
                    'rgba(0, 0, 0, 1.0)',
                    'rgba(0, 0, 0, 1.0)',
                    'rgba(0, 0, 0, 1.0)',
                    'rgba(0, 0, 0, 1.0)',
                    'rgba(0, 0, 0, 1.0)',
                    'rgba(0, 0, 0, 1.0)',

                ], width=1.5)
            ),
            text=values,
            textposition='auto',
            hovertemplate='Warehouse: %{x}<br>Pallets: %{y}<extra></extra>'
        )
    ])

    fig.update_layout(
        title=dict(
            text='Inventory by warehouse',
            font=dict(size=24, family='Verdana', weight='bold'),
            x=0.5,
            xanchor='center'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(34,34,34,0.0)',
        font=dict(
            family='Segoe UI, sans-serif',
            size=14,
            color='white'
        ),
        xaxis=dict(
            showgrid=False,
            linecolor='black',
            ticks='outside',
            tickfont = dict(
                size=16,
                color='white',
                weight='bold'
            ),
        ),
        yaxis=dict(
            title=dict(
                text='Pallets',
                font=dict(family='Verdana', weight='bold'),
            ),
            showgrid=True,
            gridcolor='rgb(216, 210, 194)',
            griddash='dashdot', #dash, dot, dashdot, longdashdot
            zeroline=True,
            zerolinecolor='grey',
        ),
        hoverlabel=dict(
            bgcolor='black',
            font_color='white',
            font_size=14,
            font_family='Verdana',
            font_weight='bold',
        ),
    )

    chart_div = to_html(fig, full_html=False, include_plotlyjs=False)
    return render(request, 'dashboards/card1.html', {"chart_div": chart_div})
