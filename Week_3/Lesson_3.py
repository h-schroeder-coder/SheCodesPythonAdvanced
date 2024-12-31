import matplotlib.pyplot as plt

lisbon_temperatures = [25, 26, 28, 24, 22]
new_york_temperatures = [15, 17, 12, 20, 22]
sydney_temperatures = [10, 12, 11, 8, 7]

days = ['Monday', 'Tuesday', 'Wednesday', "Thursday", 'Friday']

plt.style.use('Solarize_Light2')

plt.plot(days, lisbon_temperatures, label="Lisbon", marker="o", markersize=2.5, color='c')
plt.plot(days, new_york_temperatures, label="New York", marker=".", markersize=1.5, color='m')
plt.plot(days, sydney_temperatures, label="Sydney", marker="*", markersize=3, color='b')

plt.legend()
plt.xlabel("Days")
plt.ylabel("Temperatures (in celcius)")
plt.title("5-Day Weather forecast")
plt.grid(True)

plt.show()



