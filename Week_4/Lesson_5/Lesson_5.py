import csv


with open('week_4/lesson_5/customer.csv', 'r') as file:
  customers = csv.reader(file)

  for customer in customers:
    customer_number = customer[0]
    first_name = customer[2]
    last_name = customer[3]
    email = customer[9]
    print(f"Customer #{customer_number}, {first_name} {last_name}, {email}")  

