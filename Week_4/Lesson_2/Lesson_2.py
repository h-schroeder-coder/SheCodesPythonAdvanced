import csv

with open('Week_4/Lesson_2/Lesson_2_Weather.csv', 'r') as csvfile: 
    csv_reader = csv.reader(csvfile)
    
    for city in csv_reader:
        print(f"It is currently {city[2]}ºC in {city[0]}, {city[1]}")