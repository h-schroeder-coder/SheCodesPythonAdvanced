#Define a class User who receives 2 attributes in the initializer, a first name, and a last name.
class User: 
    def __init__(self, first_name, last_name):
        """Initialize the user"""
        self.first_name = first_name
        self.last_name = last_name

#Create a method called full_name, which returns the user's full name
    def full_name(self):
        """Returns a full name"""
        return f"{self.first_name} {self.last_name}"
      

#Create 2 users with 2 different names and print their full name
tessa = User("Tessa", "Lynn")
elmer = User("Elmer", "Fudd")
hadley = User("Hadley", "Jo")

#Change the first name of the first object and print the full name again

print(tessa.full_name())
print(elmer.full_name())
print(hadley.full_name())

