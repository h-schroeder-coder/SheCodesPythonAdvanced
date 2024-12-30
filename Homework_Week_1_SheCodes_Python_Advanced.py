# Create a new Weather Class

class Weather: 
    def __init__(self, name):
        """Initializes weather"""
        self.name = name
        
# Create a method called set_weather that sets the weather temperature and condition

    def set_weather(self, temperature, condition):
        """Sets the weather temperature and condition"""
        self.temperature = temperature
        self.condition = condition
        
# Create a method called display_weather(), which will display the weather information of a class object

    def display_weather(self):
        """Displays the weather info for a given class object"""
        print(f"City: {self.name}\nTemperature: {self.temperature}\nCondition: {self.condition}")
        
# Test it with some fake data such as Paris, 27, sunny

weather = Weather("Paris")
weather.set_weather(27, "Sunny")
weather.display_weather()