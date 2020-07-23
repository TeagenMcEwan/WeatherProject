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


# fig.show()

#     jsondata("data/forecast_5days_a.json")

# print(templist)


# for date in forecast_file["DailyForecasts"]:
#     date = convert_date(day["Date"])
#     min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
#     max_temp = convert_f_to_c(day["Temperature"]["Maximum"]["Value"])

#     temps = {"Date": date, "Min": min_temp, "Max": max_temp}

#     templist.append(temps)



    # date = []
    # min_temp = []
    # max_temp = []
    # min_real_feel = []
    # min_real_feel_shade = []


#     df = templist
#     import plotly.graph_objs as graph_objs

#     # x="date.append(convert_date(items["Date"]))"
#     # y="min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))"
#     # z="max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))"

# #     # min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
# #     # max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
# #     # date.append(convert_date(items["Date"]))
# #     # daytime.append(items["Day"]["LongPhrase"])
# #     # day_rain_chance.append(items["Day"]["RainProbability"])
# #     # nighttime.append(items["Night"]["LongPhrase"])
# #     # night_rain_chance.append(items["Night"]["RainProbability"])

# # # Line Graphs

# fig = px.line(df, x="min_temp" "max_temp", y="date", title="Weather Project: Minimum and Maximum Temperatures")
# fig.show()


# fig = px.line(
#     df,
#     x=["min_temp","max_temp"],
#     y=["date"],
#     title="Weather Project: Minimum and Maximum Temperatures"
# )
# fig.show()


# # df_a = {
# #     "our_data": [123, 132, 654, 345, 125, 498],
# #     "more_data": [345, 67, 176, 245, 197, 391],
# #     "columns": ["a", "b", "c", "d", "e", "f"]
# # }
# # fig = px.line(df_a, y="our_data", x="columns")
# # fig.show()

# # fig = px.scatter(
# #     df,
# #     x=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
# #     y="year"
# # )
# # fig.show()

# # # Barchart

# # fig = px.bar(df, x="year", y=["NSW"])
# # fig.show()

# # fig = px.bar(
# #     df,
# #     x="year",
# #     y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
# #     barmode="group"
# # )
# # fig.show()