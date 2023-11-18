#'Day 2: 30Days of python programming'
first_name ='Deborah'
print(first_name)
last_name = 'Koech'
print(last_name)
full_name = 'Deborah' ,'koech'
print(full_name)
is_married = False
print(is_married)
is_true = True
print(is_true)
year = 2023
print(year)
type(('Deborah'))
print(type)
first_name_length = len(first_name)
print(first_name_length)
last_name_length = len(last_name)
print(last_name_length)
if first_name_length > last_name_length:
    print("My first name is longer than last name")
elif first_name_length < last_name_length:
   print("My last name is longer than first name")   
else :
    print("My first and last name are the same length")
num_one = 5
num_two =4
diff = num_one -num_two
print(diff)
mult = num_two*num_one
print(mult)
div = num_one /num_two
print(div)
mod = num_one % num_two
print(mod)
pow = num_one ** num_two
print(pow)
floor_division = num_one // num_two
print(floor_division)   
import math
radius = 30
#calculating the are of the circle
area_of_circle = math.pi *(radius **2)
print("Area of circle is :" ,area_of_circle)
#calculating circumference
circum_circle = 2 *math.pi*radius
print("Circumference of the circle is:" ,circum_circle)
#Taking radius as user input and calculating area
user_radius = float(input("Enter the radius of the circle: "))
area_user_input = math.pi * (user_radius ** 2)
print("Area of the circle with user input radius:", area_user_input)


# Get user input for first name, last name, country, and age
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
# Displaying the collected information
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
