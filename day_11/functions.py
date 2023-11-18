#conditions 
from collections import Counter
import math


# Function to add two numbers
def add_two_numbers(a, b):
    return a + b

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius * radius

# Function to add all numbers in a variable-length argument list
def add_all_nums(*args):
    if all(isinstance(num, (int, float)) for num in args):
        return sum(args)
    else:
        return "Please provide a list of numbers."

# Function to convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to determine the season based on the month
def check_season(month):
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Winter"

# Function to calculate the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Function to solve a quadratic equation
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

# Function to print each element of a list
def print_list(my_list):
    for item in my_list:
        print(item)

# Function to reverse a list
def reverse_list(my_list):
    return my_list[::-1]

# Function to capitalize each item in a list
def capitalize_list_items(my_list):
    return [item.capitalize() for item in my_list]

# Function to add an item to the end of a list
def add_item(my_list, item):
    my_list.append(item)
    return my_list

# Function to remove an item from a list
def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list

# Function to calculate the sum of numbers in a range
def sum_of_numbers(n):
    return sum(range(1, n+1))

# Function to calculate the sum of odd numbers in a range
def sum_of_odds(n):
    return sum(range(1, n+1, 2))

# Function to calculate the sum of even numbers in a range
def sum_of_even(n):
    return sum(range(2, n+1, 2))

# Function to count evens and odds in a positive integer
def evens_and_odds(number):
    evens = sum(1 for digit in str(number) if int(digit) % 2 == 0)
    odds = len(str(number)) - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

# Function to calculate factorial of a number
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

# Function to check if a variable is empty
def is_empty(variable):
    return not bool(variable)

# Function to calculate mean of a list
def calculate_mean(my_list):
    return sum(my_list) / len(my_list)

# Function to calculate median of a list
def calculate_median(my_list):
    sorted_list = sorted(my_list)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        return sorted_list[n//2]

# Function to calculate mode of a list
def calculate_mode(my_list):
    from collections import Counter
    counts = Counter(my_list)
    max_count = max(counts.values())
    mode = [item for item, count in counts.items() if count == max_count]
    return mode

# Function to calculate range of a list
def calculate_range(my_list):
    return max(my_list) - min(my_list)

# Function to calculate variance of a list
def calculate_variance(my_list):
    mean = calculate_mean(my_list)
    squared_diff = [(x - mean)**2 for x in my_list]
    variance = sum(squared_diff) / len(my_list)
    return variance

# Function to calculate standard deviation of a list
def calculate_std(my_list):
    return math.sqrt(calculate_variance(my_list))

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Function to check if all items in a list are unique
def are_all_unique(my_list):
    return len(my_list) == len(set(my_list))

# Function to check if all items in a list have the same data type
def are_all_same_type(my_list):
    return all(isinstance(item, type(my_list[0])) for item in my_list)

# Function to check if a variable is a valid Python variable
def is_valid_variable(variable):
    import re
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None

# Example Usage
print(add_two_numbers(5, 7))
print(area_of_circle(3))
print(add_all_nums(1, 2, 3, 4, 5))
print(convert_celsius_to_fahrenheit(25))
print(check_season(6))
print(calculate_slope(1, 2, 3, 4))
print(solve_quadratic_eqn(1, -3, 2))
print(print_list(['apple', 'banana', 'cherry']))
print(reverse_list([1, 2, 3, 4, 5]))
print(capitalize_list_items(['apple', 'banana', 'cherry']))
print(add_item(['apple', 'banana', 'cherry'], 'date'))
print(remove_item(['apple', 'banana','cherry','date']))
