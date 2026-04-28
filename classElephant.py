class Animal:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        return "Animal sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Elephant(Animal):
    def speak(self):
        return f"{self.name} says Toot!"
            


my_elephant = Elephant(name="Mas")

print(my_elephant.speak())
        
