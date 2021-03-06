from urllib import request
import json
from prettytable import PrettyTable
dataTable = PrettyTable()

URL = "http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"

CITY = "seoul"
API_KEY = "d64dc55592f29a938741d0a4e3aefe76"

with request.urlopen(URL.replace("{city name}", CITY).replace("{API key}", API_KEY)) as response:
    result_json = response.read()

parsed_json = json.loads(result_json)

# print(parsed_json["weather"])
# print(parsed_json["weather"][0])
# print(parsed_json["weather"][0].keys())

dataTable.field_names = parsed_json["weather"][0].keys()

for i in parsed_json["weather"]:
    list_values = list(i.values())
    # print(list_values[0], list_values[1], list_values[2], list_values[3])
    dataTable.add_row(parsed_json["weather"][0].values())

print(dataTable)