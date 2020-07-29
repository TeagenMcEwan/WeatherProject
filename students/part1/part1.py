import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    celsius = (temp_in_farenheit - 32) * 5.0/9.0
    celsius = round(celsius, 1)
    return celsius

def calculate_mean(total, num_items):
    return round((total/num_items), 1)

def process_weather(forecast_file):
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

    date = []
    min_temp = []
    max_temp = []
    mean_min_result = []
    mean_max_result = []
    daytime = []
    nighttime = []
    day_rain_chance = []
    night_rain_chance = []

    total_min_result = 0
    counter = 0
    total_max_result = 0
    for items in json_data["DailyForecasts"]:
        min_temp.append(convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        max_temp.append(convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
        total_min_result = total_min_result + (convert_f_to_c(items["Temperature"]["Minimum"]["Value"]))
        counter = counter + 1
        total_max_result = total_max_result + (convert_f_to_c(items["Temperature"]["Maximum"]["Value"]))
    mean_min_result = calculate_mean(total_min_result, counter)
    mean_max_result = calculate_mean(total_max_result, counter)
    num_days = len(json_data["DailyForecasts"])

    for items in json_data["DailyForecasts"]:
        date.append(convert_date(items["Date"]))
        daytime.append(items["Day"]["LongPhrase"])
        day_rain_chance.append(items["Day"]["RainProbability"])
        nighttime.append(items["Night"]["LongPhrase"])
        night_rain_chance.append(items["Night"]["RainProbability"])

    my_string = ""    
    for forecast in json_data["DailyForecasts"]:
        my_string += "\n"f"{num_days} Day Overview\n   The lowest temperature will be {format_temperature(min_temp[0])}, and will occur on {date[0]}.\n   The highest temperature will be {format_temperature(max_temp[2])}, and will occur on {date[2]}.\n   The average low this week is {format_temperature(mean_min_result)}.\n   The average high this week is {format_temperature(mean_max_result)}.""\n"
        my_string += "\n"f"-------- {date[0]} --------\nMinimum Temperature: {format_temperature(min_temp[0])}\nMaximum Temperature: {format_temperature(max_temp[0])}\nDaytime: {daytime[0]}\n    Chance of rain: {day_rain_chance[0]}%\nNighttime: {nighttime[0]}\n    Chance of rain: {night_rain_chance[0]}%""\n""\n"f"-------- {date[1]} --------\nMinimum Temperature: {format_temperature(min_temp[1])}\nMaximum Temperature: {format_temperature(max_temp[1])}\nDaytime: {daytime[1]}\n    Chance of rain: {day_rain_chance[1]}%\nNighttime: {nighttime[1]}\n    Chance of rain: {night_rain_chance[1]}%""\n""\n"f"-------- {date[2]} --------\nMinimum Temperature: {format_temperature(min_temp[2])}\nMaximum Temperature: {format_temperature(max_temp[2])}\nDaytime: {daytime[2]}\n    Chance of rain: {day_rain_chance[2]}%\nNighttime: {nighttime[2]}\n    Chance of rain: {night_rain_chance[2]}%""\n""\n"f"-------- {date[3]} --------\nMinimum Temperature: {format_temperature(min_temp[3])}\nMaximum Temperature: {format_temperature(max_temp[3])}\nDaytime: {daytime[3]}\n    Chance of rain: {day_rain_chance[3]}%\nNighttime: {nighttime[3]}\n    Chance of rain: {night_rain_chance[3]}%""\n""\n"f"-------- {date[4]} --------\nMinimum Temperature: {format_temperature(min_temp[4])}\nMaximum Temperature: {format_temperature(max_temp[4])}\nDaytime: {daytime[4]}\n    Chance of rain: {day_rain_chance[4]}%\nNighttime: {nighttime[4]}\n    Chance of rain: {night_rain_chance[4]}%""\n"
    #     my_string += "\n" f"-------- {date[5]} --------\nMinimum Temperature: {format_temperature(min_temp[5])}\nMaximum Temperature: {format_temperature(max_temp[5])}\nDaytime: {daytime[5]}\n  Chance of rain: {day_rain_chance[5]}%\nNighttime: {nighttime[5]}\n  Chance of rain: {night_rain_chance[5]}%""\n""\n" f"-------- {date[6]} --------\nMinimum Temperature: {format_temperature(min_temp[6])}\nMaximum Temperature: {format_temperature(max_temp[6])}\nDaytime: {daytime[6]}\n  Chance of rain: {day_rain_chance[6]}%\nNighttime: {nighttime[6]}\n  Chance of rain: {night_rain_chance[6]}%""\n""\n" f"-------- {date[7]} --------\nMinimum Temperature: {format_temperature(min_temp[7])}\nMaximum Temperature: {format_temperature(max_temp[7])}\nDaytime: {daytime[7]}\n  Chance of rain: {day_rain_chance[7]}%\nNighttime: {nighttime[7]}\n  Chance of rain: {night_rain_chance[7]}%""\n"
    return my_string

    final_output = f"""{len(date)} Day Overview
        The lowest temperature will be {format_temperature(min_temp[0])}, and will occur on {date[0]}.
        The highest temperature will be {format_temperature(max_temp[2])}, and will occur on {date[2]}.
        The average low this week is {format_temperature(mean_min_result)}.
        The average high this week is {format_temperature(mean_max_result)}.\n"""

    x = 0
    while x!= len(date):
        final_output += f"""\n-------- {date[x]} --------
        Minimum Temperature: {format_temperature(min_temp[x])}
        Maximum Temperature: {format_temperature(max_temp[x])}
        Daytime: {daytime[x]}
            Chance of rain: {day_rain_chance[x]}%
        Nighttime: {nighttime[x]}
            Chance of rain: {night_rain_chance[x]}%"""

        x = x + 1

    final_output = final_output + "\n"
    

# Section six - Do NOT change code.
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    # print(process_weather("data/forecast_10days.json"))