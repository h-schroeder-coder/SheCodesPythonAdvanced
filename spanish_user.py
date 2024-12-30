from user2 import User
    
#Add a new class inheriting from User called SpanishUser and when greeting, it should say “Hola! - Name”
class SpanishUser(User):
    def greet(self):
        """Greets Spanish User"""
        print(f"Hola - {self.name}")