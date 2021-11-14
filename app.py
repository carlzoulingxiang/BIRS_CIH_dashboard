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




app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, '/css/button.css'])

plot_mapper = {"altair":"spec", "plotly":"figure", "cytospace":"children"}

content = html.Div([

            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Card(
                            [
                                dbc.CardHeader("Total legislator", id="lh1", style={'font-size':'20px', 'textAlign':'center'}),
                                dbc.CardBody(id="ln1", style={'font-size':'25px', 'justify-content':'center', 'align-items':'center', "display":"flex"}),
                            ], style={'height':'13vh'}),
                    ]),                 
                    
                    html.Br(),

                    dbc.Row([
                        dbc.Card(
                            [
                                dbc.CardHeader("Total topics", id="lh2", style={'font-size':'20px', 'textAlign':'center'}),
                                dbc.CardBody(id="ln2", style={'font-size':'25px', 'justify-content':'center', 'align-items':'center', "display":"flex"}),
                            ], style={'height':'13vh'})
                    ]), 
                    
                    html.Br(),

                    dbc.Row([
                        dbc.Card(
                            [
                                dbc.CardHeader("Total bills", id="lh3", style={'font-size':'20px', 'textAlign':'center'}),
                                dbc.CardBody(id="ln3", style={'font-size':'25px', 'justify-content':'center', 'align-items':'center', "display":"flex"}),
                            ], style={'height':'13vh'})
                    ]), 

                    html.Br(),

                    dbc.Row([
                        dbc.Card(
                            [
                                dbc.CardHeader("Total parties", id="lh4", style={'font-size':'20px', 'textAlign':'center'}),
                                dbc.CardBody(id="ln4", style={'font-size':'25px', 'justify-content':'center', 'align-items':'center', "display":"flex"}),
                            ], style={'height':'13vh'})
                    ]), 
                    
                    html.Br(),

                    dbc.Row([
                        dbc.Card(
                            [
                                dbc.CardHeader("Total federal bills", id="lh5", style={'font-size':'20px', 'textAlign':'center'}),
                                dbc.CardBody(id="ln5", style={'font-size':'25px', 'justify-content':'center', 'align-items':'center', "display":"flex"}),
                                dbc.Row([
                                    dbc.Col(
                                        [dbc.CardHeader("Common", id="lh5.1", style={'font-size':'10px', 'textAlign':'center'}),
                                        html.P(id="ln5_1", style={'font-size':'25px', 'textAlign':'center'}),]
                                    ),
                                    dbc.Col(
                                        [dbc.CardHeader("Senator", id="lh5.2", style={'font-size':'10px', 'textAlign':'center'}),
                                        html.P(id="ln5_2", style={'font-size':'25px', 'textAlign':'center'}),]
                                    )
                                ])                            
                            ], style={'height':'20vh'})
                    ]), 
                    
                    html.Br(),

                    dbc.Row([
                        dbc.Card(
                            [
                                dbc.CardHeader("Male / Female", id="lh6", style={'font-size':'20px', 'textAlign':'center'}),
                                dbc.CardBody(id="ln6", style={'font-size':'25px', 'justify-content':'center', 'align-items':'center', "display":"flex"}),
                            ], style={'height':'13vh', 'overflow-x': 'scroll'})
                    ]), 
                    
                ], width=2),

                dbc.Col([

                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                            dcc.RadioItems(
                                        options=[
                                            {'label': 'No. of legislators', 'value': 'l'},
                                            {'label': 'No. of bills', 'value': 'b'},
                                            {'label': 'Majority party', 'value': 'p'}
                                        ],
                                        id='click',
                                        value='b',
                                        labelClassName="date-group-labels",
                                        className="date-group-items",
                                        # inline=True,
                                    ),
                            dbc.CardBody([dcc.Graph(id="choropleth")]),
                            ], style={'height':'66vh', 'overflow-x': 'scroll'})
                            ], width=7),
                    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody(dav.VegaLite(id="f11")),
                            ], style={'height':'33vh', 'overflow-x': 'scroll'}), 
                            dbc.Card([
                                dbc.CardBody(dav.VegaLite(id="f12")),
                            ], style={'height':'33vh', 'overflow-x': 'scroll'}), 
                        ], width=5)]),
                
                    
                    dbc.Row([
                        dcc.Dropdown(id="slct_prov",
                                    options=[
                                        {"label": "BC", "value": "BC"},
                                        {"label": "ON", "value": "ON"},
                                        {"label": "AB", "value": "AB"},
                                        {"label": "QC", "value": "QC"},
                                        {"label": "MB", "value": "MB"},
                                        {"label": "NL", "value": "NL"},
                                        {"label": "NT", "value": "NT"},
                                        {"label": "SK", "value": "SK"},
                                        {"label": "NB", "value": "NB"},
                                        {"label": "YT", "value": "YT"},
                                        {"label": "PE", "value": "PE"},
                                        {"label": "NS", "value": "NS"},
                                        {"label": "NU", "value": "NU"},],
                                    multi=False,
                                    value="BC",
                                    style={'width': "40%"}),
                        
                        ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                # dbc.CardHeader(id="h21", style={'font-size':'15px', 'textAlign':'left'}),
                                dbc.CardBody(dav.VegaLite(id="f21"))], style={'height':'31vh', 'overflow-x': 'scroll'})

                            ], width=6),
                        
                        dbc.Col([
                            dbc.Card([
                                # dbc.CardHeader(id="h22", style={'font-size':'15px', 'textAlign':'left'}),
                                dbc.CardBody(dav.VegaLite(id="f22")),
                            ], style={'height':'31vh', 'overflow-x': 'scroll'}), 
                        ], width=6)
                        ]),
                ])

    
            ])

        ], style=CONTENT_STYLE)



app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
])


data_d_legton = pd.read_excel("./data/division_legislation.xlsx")
data_d_legtor = pd.read_excel("./data/division_legislator.xlsx")
data_f_legton = pd.read_excel("./data/federal_legislation.xlsx")
data_f_legtor = pd.read_excel("./data/federal_legislator.xlsx")
data_f_legtor_clean = pd.read_excel("./data/Federal_legislator_clean.xlsx")

# data_f_vote = pd.read_excel("./data/federal_bill_vote.xlsx")


    
data_merge = pd.merge(data_f_legton.groupby("province_territory").aggregate({"goverlytics_id":len}).reset_index(), 
                      data_d_legton.groupby("province_territory").aggregate({"goverlytics_id":len}).reset_index(), 
                      on="province_territory", how="outer")

data_merge["No. of bills"] = data_merge["goverlytics_id_x"].fillna(0) + data_merge["goverlytics_id_y"].fillna(0)

data_merge = pd.merge(data_merge, data_f_legtor.groupby("province_territory").aggregate({"goverlytics_id":len}).reset_index(),
                      on="province_territory", how="inner").rename({"goverlytics_id":"No. of legislators"}, axis=1)

data_f_legtor[["goverlytics_id", "party", "province_territory"]].groupby(["province_territory", "party"]).count() \
    .sort_values("goverlytics_id", ascending=False)
    
    
df_agg = data_f_legtor[["goverlytics_id", "party", "province_territory"]].groupby(["province_territory", "party"]).agg({'goverlytics_id':len})
g = df_agg['goverlytics_id'].groupby(level=0, group_keys=False)
data_merge = pd.merge(data_merge, pd.DataFrame(g.nlargest(1)).reset_index()[["province_territory", "party"]])
data_merge = data_merge[['province_territory', 'No. of bills', 'No. of legislators', 'party']]
df = pd.read_csv("./canadian_map/location_mapper.csv")
data_merge = pd.merge(data_merge, df[["province", "cartodb_id"]].rename({"province":"province_territory"}, axis=1), on="province_territory")


@app.callback(
     [
     Output(component_id='choropleth', component_property='figure'),
     ],
     [Input("click", "value"),]
)
def render_Map(color):
    
    rst = [plot_Map(color, data_input=data_merge)]
    
    return rst

@app.callback(
     [
     Output(component_id='f11', component_property='spec'),
     Output(component_id='f12', component_property='spec'),
     Output(component_id='ln1', component_property='children'),
     Output(component_id='ln2', component_property='children'),
     Output(component_id='ln3', component_property='children'),
     Output(component_id='ln4', component_property='children'),
     Output(component_id='ln5', component_property='children'),
     Output(component_id='ln5_1', component_property='children'),
     Output(component_id='ln5_2', component_property='children'),
     Output(component_id='ln6', component_property='children'),
     ],
     [Input("url", "pathname"),]
)

def render_altair_data(pathname):
    
    rst = [plot_Alice(data_input=data_f_legton)]
    rst += [plot_Nyanda(data_input=data_d_legton)]
    
    rst += [1278]
    rst += [len(set(list(data_d_legton["topic"]) + list(data_f_legton["topic"]))) - 1]
    rst += [len(set(list(data_d_legton["goverlytics_id"]) + list(data_f_legton["goverlytics_id"])))]
    rst += [len(set(list(data_d_legtor["party"]) + list(data_f_legtor["party"])))]
    rst += [300, 242, 58, "71 / 29"]
        
    return rst
    


@app.callback(
     [
    # Output(component_id='h11', component_property='children'),
    #  Output(component_id='f11', component_property='spec'),
    #  Output(component_id='h12', component_property='children'),
    #  Output(component_id='f12', component_property='spec'),
    #  Output(component_id='h13', component_property='children'),
     Output(component_id='f21', component_property='spec'),
    #  Output(component_id='h14', component_property='children'),
     Output(component_id='f22', component_property='spec'),
     ],
    [Input(component_id='slct_prov', component_property='value')]
) 

def render_altair(slct_prov):
    
    rst1 = plot_Luming(slct_prov, data_input=data_f_legtor_clean)
    rst2 = plot_Luming2(slct_prov)

    
    return [rst1, rst2]
    
    

    
if __name__ == '__main__':
    app.run_server(debug=True)