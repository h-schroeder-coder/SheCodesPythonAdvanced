import csv

with open('week_2/lesson_3/temperatures.csv', 'r') as file: 
    csv_reader = csv.reader(file)
    
    for city in csv_reader:
        #option 1
        print("-------")
        print(f"It is {city[2].lower()} and {city[1]}ºC in {city[0]}")
        ##
        print("-------")
        print(f"City: {city[0]}")
        print(f"Temperature: {city[1]}")
        print(f"Conditions: {city[2]}")
        ##
        #option 2
        city = city[0]
        temperature = city[1]
        condition = city[2].lower()
        print(f"It is currently {temperature}ºC and {condition} in {city}.")
        print("-------")