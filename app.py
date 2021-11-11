import pandas as pd
from component import *
from plot import *

import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import altair as alt
import plotly.express as px
from dash.dependencies import Input, Output
from vega_datasets import data



df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])



plot_mapper = {"altair":"spec", "plotly":"figure", "cytospace":"children"}
content = html.Div(
        [
            dbc.Row([
                gen_basic_unit(_id="01", _type="altair"),
                gen_basic_unit(_id="02", _type="altair"),
                ]),
            dbc.Row([
                gen_basic_unit(_id="11", _type="plotly"),
                gen_basic_unit(_id="12", _type="cytospace"),
                ]),
            dbc.Row([
                gen_basic_unit(_id="21", _type="altair"),
                gen_basic_unit(_id="22", _type="altair"),
                ]),
        ], style=CONTENT_STYLE,
)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])
# @app.callback(
#     Output("f01", "spec"),
#     Input("url", "pathname"),
# )
# def render_alt(pathname):
#     return plot_simple_altair_areachart("simple_altair_area_chart")

# @app.callback(
#     Output("f02", "figure"),
#     Input("url", "pathname"),
# )
# def render_px(pathname):
#     # return plot_plotly_cypto("plotly_cyptospace_chart")
#     return plot_simple_plotly_barchart("simple_plotly_bar_chart")

@app.callback(
    Output("f01", plot_mapper["altair"]),
    Output("h01", "children"),
    Output("f02", plot_mapper["altair"]),
    Output("h02", "children"),
    Output("f11", plot_mapper["plotly"]),
    Output("h11", "children"),
    Output("f12", plot_mapper["cytospace"]),
    Output("h12", "children"),
    Output("f21", plot_mapper["altair"]),
    Output("h21", "children"),
    Output("f22", plot_mapper["altair"]),
    Output("h22", "children"),
    Input("url", "pathname"),
)
def render_px(pathname):
    
    rst = []
    
    chart, title = plot_interactive_altair_scatter_dist("interactive_altair_scatter_dist")
    rst += [chart, title]
    chart, title = plot_interactive_altair_map_scatter("interactive_altair_map")
    rst += [chart, title]
    chart, title = plot_simple_plotly_barchart("simple_plotly_bar_chart")
    rst += [chart, title]
    chart, title = plot_plotly_cypto("plotly_cyptospace_chart")
    rst += [chart, title]
    chart, title = plot_simple_altair_bubblechart("simple_altair_bubble_chart")
    rst += [chart, title]
    chart, title = plot_simple_altair_areachart("simple_altair_area_chart")
    rst += [chart, title]
    
    return rst


# app.layout = html.Div([
#     dcc.Location(id="url"),
#     sidebar,
#     content
# ])

# @app.callback(
#     Output("f22", "spec"),
#     Output("f21", "spec"),
#     Output("f12", "figure"),
#     Output("f11", "figure"),
#     Output("f02", "spec"),
#     Output("f01", "spec"),
#     Input("url", "pathname"),
# )
# def render_page_content(pathname):
    
#     rst = []
    
  
#     rst += [plot_simple_altair_areachart("simple_altair_area_chart")]
#     rst += [plot_simple_altair_bubblechart("simple_altair_bubble_chart")]
#     rst += [plot_simple_plotly_barchart("simple_plotly_bar_chart")]
#     rst += [plot_plotly_cypto("plotly_cyptospace_chart")]
#     rst += [plot_interactive_altair_scatter_dist("interactive_altair_scatter_dist")]
#     rst += [plot_interactive_altair_map_scatter("interactive_altair_map")]
    
    
    
#     if pathname == "/":
        
#         pass
#         # for i, (chart_html, title) in enumerate(rst):
            
#         #     if i not in [1, 3]:
#         #         rst[i] =  [html.H1(title, style={'font-size':'18px', 'textAlign':'center'}),
#         #                    html.Iframe(
#         #                         id='plot',
#         #                         sandbox='allow-scripts',
#         #                         srcDoc=chart_html,
#         #                         style={'border-width': '0px', 'height':'40vh', 'width':'55vh'})] 
#         #     else:
#         #         rst[i] =  [html.H1(title, style={'font-size':'18px', 'textAlign':'center'}),
#         #                    dcc.Graph(id='line-chart', figure={chart_html}, config={'displayModeBar': False})]

#     return rst


if __name__ == '__main__':
    app.run_server(debug=True)