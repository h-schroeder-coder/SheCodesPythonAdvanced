#Display 2 subplots next to each other
#The first one should display the temperature deviation using a linear plot.
#The second one should display the CO2 deviation using a bar chart
#Save the result inside an image
#Make the plots look nice and readable

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle('Environmental Changes over Time')


years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

ax1.plot(years, temp_anomalies, label="Temp Anomalies (°C deviation from a baseline)", marker='o', color='c')
ax1.set_title('Changes in Temperature')
ax1.xlabel('Years')
ax1.ylabel('Temperature Anamolies (°C deviation from a baseline)')
ax1.legend()

ax2.bar(years, co2_emissions, label="CO2 Emissions (in Billions of Metric Tons)", marker='*', color='m')
ax2.set_title('Changes in CO2 Emissions')
ax2.xlabel('Years')
ax2.ylabel('CO2 Emissions in Billions of Metric Tons')
ax2.legend()

plt.savefig('output.png')
plt.show()