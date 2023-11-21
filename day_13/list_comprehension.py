#List comprehension is a compact way of creating a list from a sequence
#lambda is an anonymous function without a name ,it only has one expression.It is used to write an anonymous function inside another function
#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers= [num for num in numbers if num<=0]
print(filtered_numbers)

#Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist] #The outer loop (for sublist in list_of_lists) iterates through the outermost lists.The middle loop (for subsublist in sublist) iterates through the second-level lists.The innermost loop (for num in subsublist) iterates through the integers in the innermost lists.The num variable represents each individual integer in the innermost lists.
print(flattened_list)

list_of_tuples = [(i,1,i,i**2,i**3,i**4,i**5) for i in range(11)]
print(list_of_tuples)

#Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3], city.upper()] for country, city in sum(countries, [])]
print(flattened_countries)

#Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_dicts = [{'country':country.upper(),'city':city.upper()} for country ,city in sum (countries,[])]
print(list_dicts)

#Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [''.join(name) for name in sum(names,[])]
print(concatenated_names)

#a lambda function which can solve a slope or y-intercept of linear functions.
linear_function = lambda x, slope, intercept: slope * x + intercept
print(linear_function(2,3,4))