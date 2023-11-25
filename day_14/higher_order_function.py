#Closure is when a nested function is allowed to access the outer scope of the enclosing function
#Decorators is a design pattern that allows a user to add new functionality to an existing object without modifyingg its structure
#The map() function is a built-in function that takes a function and iterable as parameters
#The filter() function calls the specified function which returns boolean for each item of the specified iterable (list)
#reduce() function it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#defining a 'call' function before 'map'filter'or 'reduuce'
def call(func,iterable):
    return func(iterable)
result =call(sum,[1,2,3,4,5])
print(result)
#Use for loop to print each country in the countries list.

for country in countries: 
 print(country)

#Use for to print each name in the names list.
for name in names:
   print(name)

#Use for to print each number in the numbers list.
for num in numbers:
  print(num)

#Use map to create a new list by changing each country to uppercase in the countries list
countries =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def change_to_upper(country):
  return country.upper()
countries_upper_case = map(change_to_upper , countries)
print(list(countries_upper_case))

#Use map to create a new list by changing each number to its square
numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(num):
  return num**2
numbers_to_square = map(square , numbers)
print(list(numbers_to_square))

#Use map to change each name to uppercase in the names list
names =['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def change_upper(name):
  return name.upper()
names_to_upper = map(change_to_upper,names)
print(list(names_to_upper))

#Use filter to filter out countries containing 'land'.
countries =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
filtered_countries = list(filter(lambda country:'land' not in country,countries))
print(filtered_countries)
#Filter out countries having exactly six characters
filtered_countries1 = list(filter(lambda country:len(country) !=6,countries))
print(filtered_countries1)

#Use filter to filter out countries containing six letters and more in the country list.
filtered_countries2 = list(filter(lambda country:len(country) <6,countries))
print(filtered_countries2)
#Use filter to filter out countries starting with an 'E'
filtered_countries3 = list(filter(lambda country:not country.startswith('E') , countries))
print(filtered_countries3)

from functools import reduce
#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
result =(
 map(lambda x:x.upper(),filter(lambda x: 'land' not in x , countries)),
 reduce(lambda x,y: x+ ',' + y,countries)
)
print(result)

#function called get_string_lists which takes a list as a parameter and then returns a list containing only string item
def get_strings_lists(names):
  return list(filter(lambda item:isinstance(item,str),names))

#Use reduce to sum all the numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

#Use reduce to concatenate all the countries
from functools import reduce
countries =['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
concatenated_countries = reduce(lambda x,y: x+ ','+ y, countries)
sentence = f"{concatenated_countries} are nothern european countries."
print(sentence)

