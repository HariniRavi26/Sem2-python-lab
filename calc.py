class Calculator:
    def calculate(self, a=None, b=None, c=None):
        if (a is not None and type(a) not in (int, float)) or \
           (b is not None and type(b) not in (int, float)) or \
           (c is not None and type(c) not in (int, float)):
            raise ValueError("All arguments must be either integers or floats.")
        
        if a is not None and b is None and c is None:
            # If one argument is provided, return its square
            return a ** 2
        
        elif a is not None and b is not None and c is None:
            # If two arguments are provided, return their sum
            return a + b
        
        elif a is not None and b is not None and c is not None:
            # If three arguments are provided, return their product
            return a * b * c
        
        else:
            # Raise an error if the arguments don't match the constraints
            raise ValueError("You must provide 1, 2, or 3 arguments.")

calc = Calculator()


print(calc.calculate(5))  
print(calc.calculate(3, 7)) 
print(calc.calculate(2, 3, 4))  


