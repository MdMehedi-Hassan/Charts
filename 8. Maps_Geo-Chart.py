import plotly.express as px
import pandas as pd
import numpy as np

# -------------------------------
# 1. Choropleth Map
# Using built-in sample data for countries
df = px.data.gapminder().query("year==2007")
fig = px.choropleth(df, locations="iso_alpha",
                    color="gdpPercap",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Choropleth Map: GDP per Capita")
fig.show()

# -------------------------------
# 2. Bubble Map
# Locations with population size
df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df,
                     locations="iso_alpha",
                     size="pop",
                     hover_name="country",
                     projection="natural earth",
                     title="Bubble Map: Population by Country")
fig.show()

# -------------------------------
# 3. Flow Map (approximated using lines between coordinates)
# Example: major airports
flow_data = pd.DataFrame({
    "from_lat": [37.6213, 51.4700],
    "from_lon": [-122.3790, -0.4543],
    "to_lat": [40.6413, 48.8566],
    "to_lon": [-73.7781, 2.3522],
    "label": ["SFO → JFK", "LHR → Paris"]
})

fig = px.line_geo(flow_data,
                  lat=flow_data["from_lat"].tolist() + flow_data["to_lat"].tolist(),
                  lon=flow_data["from_lon"].tolist() + flow_data["to_lon"].tolist(),
                  line_group=[0,1],
                  hover_name=flow_data["label"],
                  title="Flow Map: Example Routes")
fig.update_geos(projection_type="natural earth")
fig.show()

# -------------------------------
# 4. Geospatial Heat Map
# Example: random points in USA
np.random.seed(42)
heat_df = pd.DataFrame({
    "lat": np.random.uniform(25,50,100),
    "lon": np.random.uniform(-125,-65,100)
})
fig = px.density_mapbox(heat_df, lat='lat', lon='lon', radius=10,
                        center=dict(lat=38, lon=-95),
                        zoom=3,
                        mapbox_style="stamen-terrain",
                        title="Geospatial Heat Map")
fig.show()