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
    real_feel_c = []
    real_feel_shade_c = []

def jsondata (forecast_file):
    with open(forecast_file) as f:
        forecast_file = json.load(f)


    for items in forecast_file["DailyForecast"]:
        date = date.append(convert_date(items["Date"]))
        min_temp = min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        max_temp = max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
        real_feel_c = convert_f_to_c(items["Day"] ["Temperature"])
        real_feel_shade_c = convert_f_to_c(items[""])

        temps = {"Date": date, "Min": min_temp, "Max": max_temp}

        templist.append(temps)

jsondata("data/forecast_5days_a.json")


    df = {
        "min_temps": [min_list],
        "max_temps": [max_list],
        "days": [date_list]
    }

    fig = px.line(
        df,
        x="days",
        y="min_temps", "max_temps",
        title=f"Weather Project: Minimum and Maximum Temperatures, Over {num_days} Days"
    )
    fig.write_html("first-graph.html")

fig.show()