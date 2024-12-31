import csv

with open('week_2/homework/customer_info.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    index = 0
    
    for customer in csv_reader:
        first_name = customer[2]
        last_name = customer[3]
        full_name = f"{first_name} {last_name}"
        print(f"Customer #{index + 1}, {full_name}, {customer[9]}")
        
        index = index + 1