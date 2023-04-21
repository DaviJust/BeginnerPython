"""This script contains some simple examples
What i learn:
    Learn the basics
    - Python installation: Just install visual studio code, create a py file, download the extension and run everthing on the runner. That´s all
    - Running Python scripts: Better running in the visual studio runner or a extension, because REPL is bad for big scripts and all, but u can use repl for testing
    - Using the REPL: Run your py scripts in a more faster way, is rlly good for testing new things
    - Comments: Very important u can use # or 3 "
    - Docstrings: A art of saying what u function does, actually this is very important
""" 
# Import math module 
import math

# Function to calculate square of a number 
def square(num):
    """Returns the square of a number.
    
    Args:
        num (int): The number to square
    Returns: 
        int: num squared
    """
    return num ** 2 

# Function to calculate circumference of a circle 
def circumference(radius): 
    """Calculates the circumference of a circle.
    
    Args:
        radius (int): Radius of the circle
    Returns:
        float: Circumference of the circle
    """
    return 2 * math.pi * radius 

# Check if number is even or odd
def even_or_odd(num): 
    """Determines if a number is even or odd.
    
    Args:
        num (int): Number to check
    Returns: 
        str: "Even" or "Odd"
    """
    if num % 2 == 0:
        return "Even"
    else: 
        return "Odd" 

# Run some tests in the REPL
print(square(5))   # Prints 25  
print(circumference(10)) # Prints 62.83185307179586
print(even_or_odd(3)) # Prints Odd