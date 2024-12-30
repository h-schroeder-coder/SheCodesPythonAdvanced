class User:
  def __init__(self, name):
    """initializes User"""
    self.name = name
    
  def greet(self):
    """Greets User"""
    print(f"Welcome - {self.name}")   
   