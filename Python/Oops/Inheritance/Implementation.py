# Base class for single and multilevel inheritance
class Animal:
    def speak(self):
        return "Animal sound"

# Single Inheritance: Derived class from Animal
class Dog(Animal):
    def speak(self):
        return "Bark"

# Multilevel Inheritance: Derived from Dog
class Puppy(Dog):
    def play(self):
        return "Plays with ball"

# Base classes for multiple and hybrid inheritance
class Bird:
    def fly(self):
        return "Flies"

class Swimmer:
    def swim(self):
        return "Swims"

# Multiple Inheritance: Derived from Bird and Swimmer
class Duck(Bird, Swimmer):
    def quack(self):
        return "Quack"

# Hierarchical Inheritance: Derived from Animal
class Cat(Animal):
    def speak(self):
        return "Meow"

# Hybrid Inheritance: Derived from multiple base classes
class LivingBeing:
    def live(self):
        return "Living"

class Mammal(LivingBeing):
    def warm_blooded(self):
        return "Warm-blooded"

class BirdBeing(LivingBeing):
    def lay_eggs(self):
        return "Laying eggs"

class Bat(Mammal, BirdBeing):
    def fly(self):
        return "Flying"

# Testing Single Inheritance
dog = Dog()
print(dog.speak())  # Output: Bark

# Testing Multilevel Inheritance
puppy = Puppy()
print(puppy.speak())  # Output: Bark
print(puppy.play())   # Output: Plays with ball

# Testing Multiple Inheritance
duck = Duck()
print(duck.fly())   # Output: Flies
print(duck.swim())  # Output: Swims
print(duck.quack()) # Output: Quack

# Testing Hierarchical Inheritance
cat = Cat()
print(cat.speak())  # Output: Meow

# Testing Hybrid Inheritance
bat = Bat()
print(bat.live())         # Output: Living
print(bat.warm_blooded()) # Output: Warm-blooded
print(bat.lay_eggs())     # Output: Laying eggs
print(bat.fly())          # Output: Flying
