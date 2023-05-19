import pandas as pd
import plotly.express as px
import json
from statistics import mode
with open("data/BergamoGiusto.geojson") as f:
    paesi = json.load(f)
comuni=pd.read_csv("data/ComuniFinal.csv")
SHEET_ID = '1s6ENZS_I0vm8by-VDrhtHBdNAi4kWfasjkIbFH4W5aM'
SHEET_NAME = 'Adesivi'

url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
#new=comuni.merge(df, left_on='Comune', right_on='Di che paese sei?', how='outer')
#final=new.groupby('Comune')[new.columns[3]].agg(lambda x: mode(x)).reset_index()
#final=final.fillna("Nessun Dato")

fig = px.choropleth_mapbox(df, geojson=paesi, locations="Comune", color=df.columns[1], featureidkey="properties.name", 
                           mapbox_style="carto-positron",
                           color_discrete_map={
                "Nessun Dato": "grey"},center={'lat':45.742,'lon':9.5688})
fig.write_html('pages/AdesiviPianetti.html', full_html=True)