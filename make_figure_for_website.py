#%%

import altair as alt
import pandas as pd
import altair as alt
from vega_datasets import data

# Data generators for the background
sphere = alt.sphere()
graticule = alt.graticule()

# Source of land data
source = alt.topo_feature(data.world_110m.url, 'countries')

# Layering and configuring the components
alt.layer(
    alt.Chart(sphere).mark_geoshape(fill='none'),
    alt.Chart(graticule).mark_geoshape(stroke='black', strokeWidth=0.1),
    alt.Chart(source).mark_geoshape(fill='grey', stroke='black')
).project(
    'naturalEarth1'
).properties(width=600, height=400).configure_view(strokeWidth=0.5)

# Sample data for points on the map
data0 = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060],
    'city': ['San Francisco', 'Los Angeles', 'New York']
})

# Base map configuration
background = alt.Chart(alt.Data(values=[])).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(
    type='mercator'
).properties(
    width=800,
    height=500
)

# Points on the map
points = alt.Chart(data0).mark_circle(size=100, color='red').encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    tooltip=['city:N', 'latitude:Q', 'longitude:Q']
).interactive()  # Enables zooming and panning

# Combine the map and points
map_with_points = background + points

map_with_points.save('interactive_map.html')  # Save as an HTML file
map_with_points.show()  # Display the map


# %%
