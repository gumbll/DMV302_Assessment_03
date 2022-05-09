# import libraries
import pandas as pd
import plotly.express as px

# read csv into df
col_list = ['x', 'y', 'z']
df = pd.read_csv("Data/Dataset1.csv", usecols=col_list)

# create 3d scatter plot
fig = px.scatter_3d(x=df['x'], y=df['y'], z=df['z'])
fig.show()