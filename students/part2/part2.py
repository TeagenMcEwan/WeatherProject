import json
import plotly.express as px


df = pd.read_csv("forecast_5days_a.json.csv")
# # USE FOR PROJECT! Use "Our Data" to import your own data from a json file.

# Line Graphs

fig = px.line(
    df, 
    x="Maximum Temperature"
    y="Maximum Temperature"
    title="Weather Forecast for Week of 19 June 2020"
)
fig.show()


fig = px.line(
    df,
    x="year",
    y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
    title="Australian Poplation by State"
)
fig.show()


# df_a = {
#     "our_data": [123, 132, 654, 345, 125, 498],
#     "more_data": [345, 67, 176, 245, 197, 391],
#     "columns": ["a", "b", "c", "d", "e", "f"]
# }
# fig = px.line(df_a, y="our_data", x="columns")
# fig.show()