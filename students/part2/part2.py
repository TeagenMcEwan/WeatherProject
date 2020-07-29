import json
from datetime import datetime
import plotly.express as px
import pandas as pd 


def convert_f_to_c(temp_in_farenheit):
    celsius = (temp_in_farenheit - 32) * 5.0/9.0
    celsius = round(celsius, 1)
    return celsius

# temp_in_farenheit = (temp_in_farenheit)
# tempf_to_c = int(temp_in_farenheit)
# return tempf_to_c

# templist = []

    date = []
    min_temp = []
    max_temp = []
    real_feel = []
    real_feel_shade = []

def jsondata (forecast_file):
    with open(forecast_file) as f:
        forecast_file = json.load(f)


    for items in forecast_file["DailyForecast"]:
        date = date.append(convert_date(items["Date"]))
        min_temp = min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        max_temp = max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))

        temps = {"Date": date, "Min": min_temp, "Max": max_temp}

        templist.append(temps)

    for items in forecast_file["RealFeelTemperature"]:
        real_feel = real_feel.append(convert_f_to_c(items["Minimum"]["Value"]))

    for items in forecast_file["RealFeelTemperatureShade"]:
        real_feel_shade = real_feel_shade.append(convert_f_to_c(items["Minimum"]["Value"]))

jsondata("data/forecast_5days_a.json")


df = {
    "min_temp":[min_list,
    "max_temp":[max_list],
    "date": [date_list]
    }

fig = px.line(
    df,
    x="days",
    y="temps",
    title=f"Weather Project: Minimum and Maximum Temperatures, Over {num_days} Days"
)
fig.write_html("first-graph.html")

fig.show()