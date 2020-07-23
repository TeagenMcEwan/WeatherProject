import json
import plotly.express as px
import pandas as pd 

df = pd.read_json("forecast_5days_a.json")

import plotly.graph_objects as go 

date = df["date"]
x = list("min_temp","max_temp")

line_plots = [
    go.line(x=["min_temp","max_temp"], y="date")
]

layout = go.Layout(
    title = go.layout.Title(text="Weather Project: Minimum and Maximum Temperatures", x=["min_temp","max_temp"]),
    y = convert_date(items["Date"]),
    x = convert_f_to_c(items["Temperature"]["Minimum"]["Maximum"]["Value"]),
)

fig = px.line(
    df,
    x=["min_temp","max_temp"],
    y=["date"],
    title="Weather Project: Minimum and Maximum Temperatures",
)

fig = go.Figure(data=line_plots, layout=layout)
fig = px.line(df, x="min_temp""max_temp", y="date", title="Weather Project: Minimum and Maximum Temperatures")

fig.show()