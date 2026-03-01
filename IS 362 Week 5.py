"""
I did some additional research to create this script. I felt like the weekly videos didn't
provide enough information to complete the assignment in the way I wanted to.
 """

import pandas as pd

DataFrame = pd.read_csv("airports.csv")
DataFrame.loc[417, "lat"] = 43
DataFrame.loc[417, "lon"] = -72
DataFrame.loc[417, "tzone"] = "America/New_York"
Northern_Airports = DataFrame.sort_values(by="lat", ascending=False)
Northern_Airports_Summarized = Northern_Airports[["name", "lat", "lon"]]
print(Northern_Airports_Summarized.head(5))
location_column = DataFrame["tzone"].fillna("")
country_checker = location_column.str.startswith("America")
Filtered_DataFrame = DataFrame[country_checker]
Eastern_Airports = Filtered_DataFrame.sort_values(by="lon", ascending=False)
Eastern_Airports_Summarized = Eastern_Airports[["name", "lat", "lon"]]
print(Eastern_Airports_Summarized.head(5))

DataFrame_2 = pd.read_csv("weather.csv")
DataFrame_2.loc[1009, "wind_speed"] = 0
sort_weather_1 = DataFrame_2[DataFrame_2["year"] == 2013]
sort_weather_2 = sort_weather_1[sort_weather_1["month"] == 2]
sort_weather_3 = sort_weather_2[sort_weather_2["day"] == 12]
Windiest_Locations = sort_weather_3.sort_values(by="wind_speed", ascending=False).fillna(0)
Windiest_Locations_Summarized = Windiest_Locations[["origin", "year", "month", "day", "wind_speed"]]
print(Windiest_Locations_Summarized.head(5))
