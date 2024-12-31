temperatures = [10, 12, 14, 15]

# Print the list
print(temperatures)

# Modify an existing temperature
temperatures[2] = 17



# Print the modified item
print(temperatures[2])

# Add a temperature to the list
temperatures.append(18)

# Print the the newly added item
print(temperatures)
print(temperatures[4])

forecast = {
  "Monday": { "temperature": 21, "condition": "Rainy"},
  "Tuesday": { "temperature": 20, "condition": "Sunny"},
  "Wednesday": { "temperature": 23, "condition": "Cloudy"},
  "Thursday": { "temperature": 24, "condition": "Sunny"},
}

# Print the dictionary
print(forecast)

# Modify Wednesdays temperature to 25 and Sunny
forecast["Wednesday"]["temperature"] = 25
forecast["Wednesday"]["condition"] = "Sunny"

# Print Wednesdays temperature
print(forecast['Wednesday']['temperature'])

# Add forecast for Friday, 27, Cloudy
forecast['Friday'] = { "temperature": 27, "condition": "Cloudy"}
print(forecast['Friday'])

# Print Friday temperature such as "Friday's temperature will be 27 degrees and cloudy
day = "Friday"
temperature = forecast['Friday']['temperature']
condition = forecast['Friday']["condition"].lower()
print(f"{day}'s temperature will be {temperature} degrees and {condition}")
      