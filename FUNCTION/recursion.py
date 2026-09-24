def factorial(n):
    # 1. Base Case: stops the function from running forever
    if n == 0 or n == 1:
        return 1
    
    # 2. Recursive Case: the function calls itself
    else:
        return n * factorial(n - 1)

# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
