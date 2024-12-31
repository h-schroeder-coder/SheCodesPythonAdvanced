import csv

with open('Week_4/Lesson_2/Lesson_2_Weather.csv', 'r') as csvfile: 
    reader = csv.DictReader(csvfile)
    
    for line in reader:
        print(f"It is currently {line['temperature']}ºC in {line['city']}, {line['country']}")