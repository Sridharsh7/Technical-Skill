class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Creating an instance of the Calculator class
calc = Calculator()

# Calling the add method with different numbers of arguments
print(calc.add(5))        # Output: 5
print(calc.add(5, 10))    # Output: 15
print(calc.add(5, 10, 15)) # Output: 30
