import requests
import json

api_response = requests.get(
  "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
)
# print(api_response.status_code)
if api_response.status_code != 200: print("No network connection")
data = api_response.text
parse_json = json.loads(data)
#print(parse_json)
converted = dict(parse_json)
#print(converted)


def inputDate():
  year = input('Enter a year: ')
  month = input('Enter a month: ')
  day = input("Enter a day: ")
  date = year + "-" + month + "-" + day
  return date


def get_weather_data(date):
  # print(date)
  finalValue = []
  data = converted['list']
  for i in data:
    # print(i["dt_txt"].startswith(date))
    if i["dt_txt"].startswith(date):
      result = i["dt_txt"] + " Temperatue: " + str(i["main"]["temp"])
      finalValue.append(result)
  if len(finalValue) == 0: return "Date Not Found"
  return finalValue


def get_wind_speed_data(date):
  windSpeed = []
  data = converted['list']
  for i in data:
    # print(i["dt_txt"].startswith(date))
    if i["dt_txt"].startswith(date):
      result = i["dt_txt"] + " WindSpeed: " + str(i["wind"]["speed"])
      windSpeed.append(result)
  if len(windSpeed) == 0: return "Date Not Found"
  return windSpeed


def get_pressure_data(date):
  pressure = []
  data = converted['list']
  for i in data:
    # print(i["dt_txt"].startswith(date))
    if i["dt_txt"].startswith(date):
      result = i["dt_txt"] + " Pressure: " + str(i["main"]["pressure"])
      pressure.append(result)
  if len(pressure) == 0: return "Date Not Found"
  return pressure


def main():
  while True:
    if api_response.status_code != 200: break
    print("\nMenu:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    choice = input("Enter your choice (0-3): ")

    if choice == "1":
      date = inputDate()
      print(date)
      print("Temperature: ", str(get_weather_data(date)))

    elif choice == "2":
      date = inputDate()
      print(date)
      print("Wind Speed:", get_wind_speed_data(date))

    elif choice == "3":
      date = inputDate()
      print(date)
      print("Pressure:", get_pressure_data(date))

    elif choice == "0":
      print("Exiting the program.")
      break

    else:
      print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
