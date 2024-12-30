from user2 import User

#Add a new class inheriting from User called FrenchUser and when greeting, it should say “Bonjour - Name”
class FrenchUser(User):
    def greet(self):
        """Greets French User"""
        print(f"Bonjour - {self.name}")  