import dash
import dash_bootstrap_components as dbc
import dash_alternative_viz as dav
from dash import html
from dash import dcc

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


sidebar = html.Div(
    [
        html.Img(src="./assets/mds-hex-sticker-small.png", height="15%", style={"display":"block", "margin":"0 auto"}),
        # html.H1("UBC-MDS", className="display-1", style={'font-size':'25px', 'textAlign':'center'}),
        html.H1("Tratadores", className="display-1", style={'font-size':'25px', 'textAlign':'center'}),
        html.Hr(),
        html.P(
            "We can add some note here...", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Page0", href="/", active="exact"),  ##exact mean when url is equal to href, then it is active
                dbc.NavLink("Page1", href="/page-1", active="exact"),
                dbc.NavLink("Page2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        )
    ],
    style=SIDEBAR_STYLE,
)



def gen_basic_unit(_id, _type, style={'height':'30vh', 'overflow-x': 'scroll'}):
    
    if _type == "altair":
        
        return dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader(id="h"+_id, style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dav.VegaLite(id="f"+_id)),
                    ], style=style)
                ], width=5)
        
    elif _type == "plotly":
        
        return dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader(id="h"+_id, style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(dcc.Graph(id="f"+_id)),
                    ], style=style)
                ], width=5)
        
    elif _type == "cytospace":
        
        return dbc.Col([
                dbc.Card(
                    [
                        dbc.CardHeader(id="h"+_id, style={'font-size':'15px', 'textAlign':'left'}),
                        dbc.CardBody(html.Div(id="f"+_id)),
                    ], style=style)
                ], width=5)
        






# content_unit_altair = html.Div(
#     [
#         dbc.Row(
#             [
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardBody(id='alt11', children=[]),
#                     ]),
#                 ], width=5),
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardBody(id='alt12', children=[]),
#                     ]),
#                 ], width=5),
#             ],
#             className='mb-2'
#         )
#     ],
#     style=CONTENT_STYLE,
# )


# content = html.Div(
#     [dbc.Row(
#             [
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardBody(id=f'alt{i}1', children=[]),
#                     ]),
#                 ], width=5),
#                 dbc.Col([
#                     dbc.Card([
#                         dbc.CardBody(id=f'alt{i}2', children=[]),
#                     ]),
#                 ], width=5),
#             ],
#             className='mb-2'
#         ) \
#      for i in range(4)
#     ],
#     style=CONTENT_STYLE,
# )