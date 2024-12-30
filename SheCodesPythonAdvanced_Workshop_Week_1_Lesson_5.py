#Define a class called User, which receives the first name and the year of birth
class User: 
    """Defines a User"""

    #Create a method called “Welcome” which should display “Welcome Name, you were born during the 20th century” or 21st if the user was born after 2000
    def __init__(self, name, birth_year):
        """Initialize a User with a name and birth year"""
        self.name = name
        self.birth_year = birth_year
        
    def welcome(self):
        """Welcomes user based on birth year"""
        if self.birth_year < 2000:
            return f"Welcome {self.name}, you were born during the 20th century"
        else:
            return f"Welcome {self.name}, you were born during the 21st century"
    
#Welcome 2 users to test this out

linda = User("Linda", 1965)
noelle = User("Noelle", 2021)

print(linda.welcome())
print(noelle.welcome())