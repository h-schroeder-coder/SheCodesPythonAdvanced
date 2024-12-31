import csv

with open('week_2/lesson_5/cities.csv', 'r') as file:
    csv_reader = csv.reader(file)
    try:
        for city in csv_reader:
            print(f"- It is {city[1]}ºC in {city[0]}")
    except IndexError:
        print("-- no data available")

    