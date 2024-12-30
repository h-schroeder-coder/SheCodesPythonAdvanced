#Define a class User who receives 2 attributes in the initializer, a first name, and a last name.
class User: 
    def __init__(self, firstname, lastname):
        """Initialize the user"""
        self.firstname = firstname
        self.lastname = lastname

#Create a method called full_name, which returns the user's full name
    def full_name(self):
        """Returns a full name"""
        print(f"{self.firstname} {self.lastname}")


#Create 2 users with 2 different names and print their full name
tessa = User("Tessa", "Lynn")
elmer = User("Elmer", "Fudd")
hadley = User("Hadley", "Jo")

#Change the first name of the first object and print the full name again

tessa.full_name()
elmer.full_name()
hadley.full_name()