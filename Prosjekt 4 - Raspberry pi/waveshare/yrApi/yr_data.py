"""
Børre Stellander
json from yr. Location Remmen, Halden:  lat: 59.1304, lon: 11.3546, altitude: ca. 80
    https://api.met.no/weatherapi/locationforecast/2.0/#!/data/get_compact_format

    request api: https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=80&lat=63.4305&lon=10.3950
    curl: curl -X GET --header 'Accept: application/json' 'https://api.met.no/weatherapi/locationforecast/2.0/compact?altitude=80&lat=59.1304&lon=11.3545'
 """

import requests  # api module
import json     #Save as Json

#Remmen location og altitude:
lat = "59.1304"
lon = "11.3546"
alt = "80"

# url to yr api
url = "https://api.met.no/weatherapi/locationforecast/2.0/complete.json?altitude=" + alt + "&lat=" + lat + "&lon=" + lon

# Header to tell yr where the request is coming from.
# NB! Find your user-agent and put the feeld
headers = {
    "Content-type": "application/json",
    "Cache-Control": "no-cache",
    "user-agent": "Put your user-agent here"
}

# get the json api
response = requests.request("GET", url, headers=headers)
if response:
    print('Success!')
else:
    print('An error has occurred.')
data = response.json()

def write_json_file():
    """ Save data as json file """
    with open('yr_data_complete_format.json', 'w') as f:
        json.dump(data, f)

write_json_file()

# TODO! If-Modified-Since
def updated_time():
    """ Time updated at yr """
    updated = (data["properties"]["meta"]["updated_at"])
    return updated

#print(data["properties"]["timeseries"][0]["data"]["instant"]["details"])

def air_temperature():
    """ Return the instant air temperature in celsius """
    air_temp = (data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])
    return air_temp


def wind_speed():
    """ Wind speed in m/s """
    wind_speed = (data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_speed"])
    return wind_speed


# Precentage value of the total cloud cover at all heights
cloud_area = (data["properties"]["timeseries"][0]["data"]["instant"]["details"]["cloud_area_fraction"])
rel_humidity = (data["properties"]["timeseries"][0]["data"]["instant"]["details"]["relative_humidity"])

def summary_1_hour():
    """ String value giving a summary for +1 hour """
    summary_1_hour = (data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"])
    return summary_1_hour

def precipitation_1_hour():
    """ Precipitation for +1 hour in mm """
    precipitation_1_hour = (data["properties"]["timeseries"][0]["data"]["next_1_hours"]["details"]["precipitation_amount"])
    return precipitation_1_hour

def wind_direction():
    """ Return the wind from direction """
    wind_from_direction = (data["properties"]["timeseries"][0]["data"]["instant"]["details"]["wind_from_direction"])
    if wind_from_direction > 326.25 or wind_from_direction < 11.25:
        print("Nord")
        return "North"
    elif wind_from_direction < 56.25:
        print("Nordøst")
        return "Northeast"
    elif wind_from_direction < 101.25:
        print("Øst")
        return "East"
    elif wind_from_direction < 146.25:
        print("Sørøst")
        return "Southeast"
    elif wind_from_direction < 191.25:
        print("Sør")
        return "South"
    elif wind_from_direction < 236.25:
        print("Sørvest")
        return "Southwest"
    elif wind_from_direction < 281.25:
        print("Vest")
        return "West"
    elif wind_from_direction < 326.25:
        print("Nordvest")
        return "Northwest"

#print(wind_direction())

