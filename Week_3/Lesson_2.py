import matplotlib.pyplot as plt

day = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
lisbon_temperature = [25, 24, 23, 20, 18]
new_york_temperature = [0, -1, 5, 3, -2]
sydney_temperature = [28, 30, 32, 27, 35]

plt.plot(day, lisbon_temperature)
plt.plot(day, new_york_temperature)
plt.plot(day, sydney_temperature)

plt.title("Forecasted Temperatures in 3 Cities")
plt.xlabel('Day')
plt.ylabel('Temperature (in Degrees Celcius)')
plt.legend(["Lisbon", "New York", "Sydney"])


plt.show()