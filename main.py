# Weather Forecast Application Script
# import the forecast module to use the CityForecast class
import forecast

# create objects for each city and their forecast
new_york = forecast.CityForecast("New York", 70, "Sunny", 50)
london = forecast.CityForecast("London", 60, "Cloudy", 65)
tokyo = forecast.CityForecast("Tokyo", 75, "Rainy", 70)

# store the objects into a list
list_of_cities = [new_york, london, tokyo]

# put the user through a loop for them to check multiple forecasts
while True:
    city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
    city = city.lower()

    # option to exit the app
    if city == 'exit':
            break

    # if the user doesn't exit, display their desired city forecast
    else:
        city_found = False

        # loop through the list of cities
        for i in list_of_cities:

            # if the city matches user input set city_found to True and break the loop
            if i.get_city_name().lower() == city:
                city_found = True
                break
        # if the users input matches one of the cities, display the forecast of the city found in the previous loop
        if city_found == True:
            print(i.display_forecast())
        # if user enters a city not listed, display appropriate feedback
        else:
            print("City data not found.")