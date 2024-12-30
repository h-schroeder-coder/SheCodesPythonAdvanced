class User:
  def __init__(self, name):
    """initializes User"""
    self.name = name
    
  def greet(self):
    """Greets User"""
    print(f"Welcome - {self.name}")   
   
#Add a new class inheriting from User called FrenchUser and when greeting, it should say “Bonjour - Name”
class FrenchUser(User):
    def greet(self):
        """Greets French User"""
        print(f"Bonjour - {self.name}")  

#Add a new class inheriting from User called SpanishUser and when greeting, it should say “Hola! - Name”
class SpanishUser(User):
    def greet(self):
        """Greets Spanish User"""
        print(f"Hola - {self.name}")
        
 #Test both classes
    

pau = SpanishUser("Pau")
sosthene = FrenchUser("Sosthene")

pau.greet()
sosthene.greet()

#Move each class into their files

