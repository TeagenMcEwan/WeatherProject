import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# Section one - already completed.
def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

    # """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    # Args:
    #     temp: A string representing a temperature.
    # Returns:
    #     A string contain the temperature and 'degrees celcius.'
    # """


# Section two - already completed.
def convert_date(iso_string):

    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

    # """Converts and ISO formatted date into a human readable format.
    
    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year
    # """


# Section three - add code.
def convert_f_to_c(temp_in_farenheit):

    celsius = (temp_in_farenheit - 32) * 5.0/9.0
    celsius = round(celsius, 1)
    return celsius

    # """Converts an temperature from farenheit to celcius

    # Args:
    #     temp_in_farenheit: integer representing a temperature.
    # Returns:
    #     An integer representing a temperature in degrees celcius.
    # """

# (enter function here)
# create a new variable - Use formula to convert to celcius - variable output
# return variable output. This will produce more opportuites to enter in more information and output more results.
# Use the "round function" to bring the temperatiure to one decimal place. 


# Section four - add code.
def calculate_mean(total, num_items):
    return round((total/num_items), 1)

    # """Calculates the mean.
    
    # Args:
    #     total: integer representing the sum of the numbers.
    #     num_items: integer representing the number of items counted.
    # Returns:
    #     An integer representing the mean of the numbers.
    # """


# Section five - add code.
    # """Converts raw weather data into meaningful text.

    # Args:
    #     forecast_file: A string representing the file path to a file
    #         containing raw weather data.
    # Returns:
    #     A string containing the processed and formatted weather data.
    # """


# Import the data (forecast data)

def process_weather(forecast_file):

    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

# Look at expected output file to see what information I need to grab from the data file. 
# Use forecast_expected_Output.txt file headings.
# Get the data from the forecast_5days_a_jason
# The code that I write has to include a function that pulls the data. ie for loop.
# Insert a for loop, so that the daily information is provided. 
# Insert a for loop and relate it back to 5 days or 10 days of data.
# "\n" will ensure items are on one seperate line each and not in sentences. 
# When runnning the terminal python will use forecast_5days data.

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
    my_string += "\n" f"{num_days} Day Overview\n   The lowest temperature will be {format_temperature(min_temp[0])}, and will occur on {date[0]}.\n   The highest temperature will be {format_temperature(max_temp[2])}, and will occur on {date[2]}.\n   The average low this week is {format_temperature(mean_min_result)}.\n   The average high this week is {format_temperature(mean_max_result)}.""\n"
    my_string += "\n" f"-------- {date[0]} --------\n Minimum Temperature: {format_temperature(min_temp[0])}\n Maximum Temperature: {format_temperature(max_temp[0])}\n Daytime: {daytime[0]}\n     Chance of rain: {day_rain_chance[0]}%\n Nighttime: {nighttime[0]}\n     Chance of rain: {night_rain_chance[0]}%""\n" "\n" f"-------- {date[1]} --------\n Minimum Temperature: {format_temperature(min_temp[1])}\n Maximum Temperature: {format_temperature(max_temp[1])}\n Daytime: {daytime[1]}\n     Chance of rain: {day_rain_chance[1]}%\n Nighttime: {nighttime[1]}\n     Chance of rain: {night_rain_chance[1]}%""\n" "\n" f"-------- {date[2]} --------\n Minimum Temperature: {format_temperature(min_temp[2])}\n Maximum Temperature: {format_temperature(max_temp[2])}\n Daytime: {daytime[2]}\n     Chance of rain: {day_rain_chance[2]}%\n Nighttime: {nighttime[2]}\n     Chance of rain: {night_rain_chance[2]}%""\n" "\n" f"-------- {date[3]} --------\n Minimum Temperature: {format_temperature(min_temp[3])}\n Maximum Temperature: {format_temperature(max_temp[3])}\n Daytime: {daytime[3]}\n     Chance of rain: {day_rain_chance[3]}%\n Nighttime: {nighttime[3]}\n     Chance of rain: {night_rain_chance[3]}%""\n" "\n" f"-------- {date[4]} --------\n Minimum Temperature: {format_temperature(min_temp[4])}\n Maximum Temperature: {format_temperature(max_temp[4])}\n Daytime: {daytime[4]}\n     Chance of rain: {day_rain_chance[4]}%\n Nighttime: {nighttime[4]}\n     Chance of rain: {night_rain_chance[4]}%""\n"
    # my_string += "\n" f"-------- {date[5]} --------\n Minimum Temperature: {format_temperature(min_temp[5])}\n Maximum Temperature: {format_temperature(max_temp[5])}\n Daytime: {daytime[5]}\n     Chance of rain: {day_rain_chance[5]}%\n Nighttime: {nighttime[5]}\n     Chance of rain: {night_rain_chance[5]}%""\n" "\n" f"-------- {date[6]} --------\n Minimum Temperature: {format_temperature(min_temp[6])}\n Maximum Temperature: {format_temperature(max_temp[6])}\n Daytime: {daytime[6]}\n     Chance of rain: {day_rain_chance[6]}%\n Nighttime: {nighttime[6]}\n     Chance of rain: {night_rain_chance[6]}%""\n" "\n" f"-------- {date[7]} --------\n Minimum Temperature: {format_temperature(min_temp[7])}\n Maximum Temperature: {format_temperature(max_temp[7])}\n Daytime: {daytime[7]}\n     Chance of rain: {day_rain_chance[7]}%\n Nighttime: {nighttime[7]}\n     Chance of rain: {night_rain_chance[7]}%""\n"
    
    return my_string

    
# Section six - Do NOT change code.
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    # print(process_weather("data/forecast_10days.json"))
# Note: 8days.json file is titled _10days.json file