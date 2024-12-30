class User():
  def __init__(self, name):
    self.name = name
    
  def greet(self):
    if self.type === "french":
        print(f"Bonjour - {self.name}")  
    else :
        print(f"Hola - {self.name}")

#Add a new class inheriting from User called FrenchUser and when greeting, it should say “Bonjour - Name”
class FrenchUser(User):
    def __init__(self, name):
       self.name = name
       self.type = french
       
    

#Add a new class inheriting from User called SpanishUser and when greeting, it should say “Hola! - Name”
class SpanishUser(User):
    def __init__(self, name):
        self.name = name
        self.type = spanish
        
 #Test both classes
    

pau = SpanishUser("Pau")
sosthene = FrenchUser("Sosthene")

pau.greet()
sosthene.gree()

#Move each class into their files

