#!/usr/bin/env python3
"""
Simple Python Example
A basic script demonstrating fundamental Python concepts
"""

def greet_user(name):
    """Function to greet a user with their name"""
    return f"Hello, {name}! Welcome to Python programming!"

def calculate_factorial(n):
    """Calculate factorial of a number using a loop"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

def list_operations():
    """Demonstrate list operations"""
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]
    print(f"Original list: {numbers}")
    
    # Add some numbers
    numbers.extend([6, 7, 8])
    print(f"After extending: {numbers}")
    
    # List comprehension to get squares
    squares = [x**2 for x in numbers]
    print(f"Squares: {squares}")
    
    # Filter even numbers
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")

def main():
    """Main function to run the example"""
    print("=" * 50)
    print("      Simple Python Example")
    print("=" * 50)
    
    # Basic variables
    name = "Python Learner"
    age = 25
    height = 5.8
    is_student = True
    
    print(f"\nVariable Examples:")
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
    
    # Function examples
    print(f"\nFunction Examples:")
    greeting = greet_user(name)
    print(greeting)
    
    # Calculate factorial
    number = 5
    factorial_result = calculate_factorial(number)
    print(f"Factorial of {number} is: {factorial_result}")
    
    # List operations
    print(f"\nList Operations:")
    list_operations()
    
    # Dictionary example
    print(f"\nDictionary Example:")
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"]
    }
    
    print(f"Person info: {person}")
    print(f"Name: {person['name']}")
    print(f"Hobbies: {', '.join(person['hobbies'])}")
    
    # Conditional statements
    print(f"\nConditional Examples:")
    temperature = 22
    if temperature > 25:
        weather = "hot"
    elif temperature > 15:
        weather = "pleasant"
    else:
        weather = "cold"
    
    print(f"Temperature: {temperature}°C - Weather is {weather}")
    
    # Loop examples
    print(f"\nLoop Examples:")
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(f"  Count: {i}")
    
    # While loop example
    print("Countdown from 3:")
    countdown = 3
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1
    print("  Blast off! 🚀")
    
    print(f"\n" + "=" * 50)
    print("Example completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()