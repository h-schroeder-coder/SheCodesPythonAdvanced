def calculate_total_population(populations):
  """calculates the total population given a list of countries and populations"""
  
  total = 0
  for location in populations: 
    total = total + int(location['population'])
    
  return total
    
def display_calculated_rounded_total_population(total):
  """displays the rounded total population in millions, rounded"""
  total_in_millions = round(total / 1000000)
  
  print(f"The total population is {total_in_millions} million people")


#initial data set
populations = [
  { 'country': "France", "population": "60000000"},
  { 'country': "Spain", "population": "50000000"},
  { 'country': "USA", "population": "30000000"},
  { 'country': "Australia", "population": "25000000"},
  { 'country': "Canada", "population": "38000000"},
]

# Display the total population such as, the total population is 203 million people

total_population = calculate_total_population(populations)
display_calculated_rounded_total_population(total_population)

