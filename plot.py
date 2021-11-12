import json
import altair as alt
import plotly.express as px
import dash_cytoscape as cyto
from vega_datasets import data



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
