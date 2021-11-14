import json
import pandas as pd
import altair as alt
import plotly.express as px
import dash_cytoscape as cyto
from vega_datasets import data


alt.data_transformers.enable('data_server')

def plot_Alice(data_input):
    F_new=data_input[['province_territory', 'topic']].dropna().copy()
    F_new = F_new[F_new['province_territory']!='None']
    F_new.loc[:, "topic"] = F_new.loc[:, "topic"].replace("government operations", "government")
    
    #Federal_null
    alt_chart = alt.Chart(F_new, title=alt.TitleParams(
        text='Relevant Issues per Province',
        subtitle='Ontarians & Quebecois Care the Most About Law & Crime')).mark_rect().encode(
    alt.X('topic', sort='y', title = "Topic"),
    alt.Y('province_territory', title = "Province", sort = 'x'),
    alt.Tooltip('count()'),
    color = 'count()',
    ).properties(
        width=350,
        height=160,
    ).configure_axis(
    labelFontSize=12,                                                 # Change the font size of the axis labels (the numbers)                                                  # Change the font size of the axis title                                                  # Change the font size of the legend title                                                      # Change the font size of the chart title
    )
    
    return (alt_chart.to_dict())

def plot_Nyanda(data_input):
    
    div_leg_new = data_input[["province_territory", "topic"]].dropna()
    alt_chart = alt.Chart(div_leg_new, title=alt.TitleParams(
            text='Division-Level: Relevant Issues per Province',
            subtitle='New Brunswickers Care more about Government Operations & Nova Scotians about Health')).mark_square(size=100).encode(
        alt.X('topic', sort='y', title = "Topic"),
        alt.Y('province_territory', title = "Province", sort = 'x'),
        alt.Tooltip('count()'),
        alt.Color('count()', scale=alt.Scale(scheme='viridis', reverse=True))
    ).properties(
        width=350,
        height=160,
    ).configure_axis(
    labelFontSize=12,                                                 # Change the font size of the axis labels (the numbers)                                                  # Change the font size of the axis title                                                  # Change the font size of the legend title                                                      # Change the font size of the chart title
    )
    
    return (alt_chart.to_dict())


def plot_Luming(province, data_input):
    # Plot the sorted and filtered data frame
    # data_input["years_active"] = data_input["years_active"].apply(len)
    data_nna = data_input.loc[:,["province_territory", "gender", "party"]].dropna()
    data_bc = data_nna[data_nna['province_territory'] ==province]
    chart_1 = alt.Chart(data_bc, title = "Number of legislators for Male and Female").mark_bar().encode(
        y = alt.Y("party", sort = "-x"),
        x = alt.X("count()"),
        color = "gender").properties(
        width = 300,
        height = 200)

    
    return chart_1.to_dict()

def plot_Luming2(province):
    data_df = pd.read_excel("./data/Federal_legislator_clean.xlsx")
    data_df = data_df[data_df['province_territory'] ==province]
    years_active = data_df.loc[:,['years_active', "gender", 'party']].query('years_active != 2012').dropna()

    chart_2 = alt.Chart(years_active, title=alt.TitleParams(text="Number of Active Years per Legislator",
            subtitle='Liberals Outpace Legislators in Years of Service')).mark_point().encode(
        alt.X("years_active", bin=alt.Bin(maxbins=30), title = "Years active"),
        alt.Y("party", title = "Party"),
        alt.Tooltip("count()"),
        size = "count()",
        fill = "party",
        color = "party"
        
    ).properties(
        width = 300,
        height = 200
    )
    
    return chart_2.to_dict()


def handle_cate_bill(x):
    
    if x<10:
        return "1-10"
    elif x<30:
        return "10-30"
    elif x<50:
        return "30-50"
    elif x<100:
        return "50-100"
    elif x<250:
        return "100-250"
    elif x<300:
        return "250-300"
    else:
        return ">300"

def handle_cate_legislator(x):
    
    if x<5:
        return "1-5"
    elif x<20:
        return "5-20"
    elif x<35:
        return "20-35"
    elif x<50:
        return "35-50"
    elif x<65:
        return "50-65"
    elif x<80:
        return "65-80"
    else:
        return ">80"        

def plot_Map(color, data_input):
    
    data_merge = data_input
    
    with open("./canadian_map/canada_provinces.geojson", "r") as geo:
        mp = json.load(geo)

    data_merge["No. of bills level"] = data_merge["No. of bills"].apply(handle_cate_bill)
    data_merge["No. of legislators level"] = data_merge["No. of legislators"].apply(handle_cate_legislator)
    cols = {x:x.replace(" ", "_").replace(".", "") for x in data_merge.columns}
    data_merge = data_merge.rename(cols, axis=1)
    print(data_merge.columns)
    
    if color=='l':

        fig = px.choropleth(data_merge,
                            locations="cartodb_id",
                            geojson=mp,
                            featureidkey="properties.cartodb_id",
                            color="No_of_legislators_level",
                            color_discrete_map={
                                '1-5': '#fffcfc',
                                '5-20' : '#ffdbdb',
                                '20-35' : '#ffbaba',
                                '35-50' : '#ff9e9e',
                                '50-65' : '#ff7373',
                                '65-80' : '#ff4d4d',
                                '>80' : '#ff0d0d'},
                            category_orders={
                            'No_of_legislators_level' : [
                                '1-5',
                                '5-20',
                                '20-35',
                                '35-50',
                                '50-65',
                                '65-80',
                                '>80'
                            ]
                            },
                            # animation_frame="timeframe",
                            scope='north america',
                            title='<b>Overiview of Canada politics</b>',
                            labels={'No_of_bills_level' : 'No. of bills',
                                    'No_of_legislators_level ' : 'No. of legislators '},
                            hover_name='province_territory',
                            hover_data={
                                'No_of_bills' : True,
                                'No_of_legislators' : True,
                                'party': True
                            },
                            height=500,
                            locationmode='geojson-id',
                            )
    elif color == 'b':
        
        fig = px.choropleth(data_merge,
                    locations="cartodb_id",
                    geojson=mp,
                    featureidkey="properties.cartodb_id",
                    color="No_of_bills_level",
                    color_discrete_map={
                        '1-10': '#fffcfc',
                        '10-30' : '#ffdbdb',
                        '30-50' : '#ffbaba',
                        '50-100' : '#ff9e9e',
                        '100-250' : '#ff7373',
                        '250-300' : '#ff4d4d',
                        '>300' : '#ff0d0d'},
                    category_orders={
                      'No_of_bills_level' : [
                          '1-10',
                          '10-30',
                          '30-50',
                          '50-100',
                          '100-250',
                          '250-300',
                          '>300'
                      ]
                    },
                    # animation_frame="timeframe",
                    scope='north america',
                    title='<b>Overiview of Canada politics</b>',
                    labels={'No_of_bills_level' : 'No. of bills',
                            'No_of_legislators_level ' : 'No. of legislators '},
                    hover_name='province_territory',
                    hover_data={
                        'No_of_bills' : True,
                        'No_of_legislators' : True,
                        'party': True
                    },
                    height=500,
                    locationmode='geojson-id',
                    )
    else:
        
        fig = px.choropleth(data_merge,
                    locations="cartodb_id",
                    geojson=mp,
                    featureidkey="properties.cartodb_id",
                    color="party",
                    # animation_frame="timeframe",
                    scope='north america',
                    title='<b>Overiview of Canada politics</b>',
                    labels={'No_of_bills_level' : 'No. of bills',
                            'No_of_legislators_level ' : 'No. of legislators '},
                    hover_name='province_territory',
                    hover_data={
                        'No_of_bills' : True,
                        'No_of_legislators' : True,
                        'party': True
                    },
                    height=500,
                    locationmode='geojson-id',
                    )
        
    return fig


def plot_pie(data_input):
    
    fig_pie = px.pie(data_input[data_input["gender_x"].notna()], names="gender_x",
                 color_discrete_sequence=['#334668','#496595'])
    return fig_pie

# def plot_Luming(data_input):
#     return interact(scatter_plot, province=data_input['province_territory'].unique().tolist()).embed(max_opts=100)

def plot_interactive_altair_scatter_dist(title):
    source = data.cars()
    brush = alt.selection(type='interval')
    points = alt.Chart(source).mark_point().encode(
        x='Horsepower:Q',
        y='Miles_per_Gallon:Q',
        color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
    ).add_selection(
        brush
    ).properties(
        width=300,
        height=150,
    )

    bars = alt.Chart(source).mark_bar().encode(
        y='Origin:N',
        color='Origin:N',
        x='count(Origin):Q'
    ).transform_filter(
        brush
    ).properties(
        width=300,
        height=50,
    )

    alt_chart = (points & bars)
    return (alt_chart.to_dict()), title


def plot_interactive_altair_map_scatter(title):
    
    source = data.zipcodes.url

    alt_chart = alt.Chart(source).transform_calculate(
        "leading digit", alt.expr.substring(alt.datum.zip_code, 0, 1)
    ).mark_circle(size=3).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color='leading digit:N',
        tooltip='zip_code:N'
    ).project(
        type='albersUsa'
    ).properties(
        width=350,
        height=300,
    )  
    
    return (alt_chart.to_dict()), title
    
def plot_simple_plotly_barchart(title):
    
    import pandas as pd
    
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    
    return fig, title

def plot_simple_altair_areachart(title):
    
    source = data.stocks()

    alt_chart = alt.Chart(source).transform_filter(
        'datum.symbol==="GOOG"'
    ).mark_area(
        line={'color':'darkgreen'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='white', offset=0),
                alt.GradientStop(color='darkgreen', offset=1)],
            x1=1,
            x2=1,
            y1=1,
            y2=0
        )
    ).encode(
        alt.X('date:T'),
        alt.Y('price:Q')
    ).properties(
        width=350,
        height=300,
    )  
    
    
    return alt_chart.to_dict(), title


def plot_simple_altair_bubblechart(title):
    
    source = data.cars()

    alt_chart = alt.Chart(source).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        size='Acceleration',
        color='Origin'
    ).properties(
        width=350,
        height=300,
    )  

    return alt_chart.to_dict(), title
 

def plot_plotly_cypto(title):
    
    with open('./assets/computersci-data.json', 'r') as f:
        elements = json.loads(f.read())

    # Load stylesheet
    with open('./assets/computersci-style.json', 'r') as f:
        stylesheet = json.loads(f.read())
    
    fig = cyto.Cytoscape(
        id = 'cytoscape',
        elements = elements,
        layout={'name': 'preset'},

        stylesheet = stylesheet,
        style={
            'width': '80%',
            'height': '750px',
            'position': 'absolute',
            #'background-color': '#0A0A0A',
            'left': 0,
            'top': 0,
            'z-index': 999
        }
    )
    
    return fig, title

def plot_big_altair(title):
    source = data.jobs()
    lines = alt.Chart(source).mark_line().encode(
        x='year:T',
        y='count:Q',
        color='sex'
    ).properties(
        width=300,
        height=150,
    )

    alt_chart = lines
    return (alt_chart.to_dict()), title
