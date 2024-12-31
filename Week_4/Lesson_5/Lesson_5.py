import csv

def display_customer_info(customer):
  """Show data from customer csv file"""
  customer_number = customer[0]
  first_name = customer[2]
  last_name = customer[3]
  email = customer[9]
  print(f"Customer #{customer_number}, {first_name} {last_name}, {email}")  


"""Loop through each line from customer.csv file and display each customer's number, first and last name, and email"""
with open('week_4/lesson_5/customer.csv', 'r') as customer_file:
  customers = csv.reader(customer_file)

  for customer in customers:
    display_customer_info(customer)  

