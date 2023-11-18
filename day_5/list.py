#List is a collection of data types which is ordered and changeable(modifiable).It also allows duplicate members
empty_list = [] #declare an empty list
five_items = [1,2,3,4,5]
print(len(five_items))
first_item = five_items[0]
middle_item =five_items[len(five_items)//2] #finding the middle item
last_item = five_items[-1]
#declaring a list of mixed data types
mixed_data_types =['name',age,height,'marital status',adress]
name = 'Deborah'
age = 21
height = 154 
marital_status = 'single'

it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle']
print(it_companies)
print(len(it_companies))
first_no =it_companies[0]
print(first_no)
middle_no = it_companies[len(it_companies)//2]
print(middle_no)
last_no = it_companies[-1]
print(last_no)

#printing the list after modification
it_companies[0] = 'Instagram'
print(it_companies)
it_companies.insert(len(it_companies)//2, 'Twitter')
it_companies[4] = it_companies[4].upper #change company at index 4 to upper

joint_companies = '#'.join(it_companies)# joining it_companies using '#' symbol
print(joint_companies)

company_exists = 'Bolt' in it_companies
print(company_exists)

it_companies.sort()
it_companies.reverse()

#slicing out the first 3 companies
first_3_companies = it_companies[:3]
print(first_3_companies)
#slicing out the last 3 companies
last_3_companies = it_companies[-3:]

it_companies.pop(0)# removing first company on the list
it_companies.pop(len(it_companies)//2)#removing the middle company on the list
it_companies.pop(-1)#removing last item
del it_companies# destryoing the It company list

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end+back_end
print(full_stack)
full_stack.insert(full_stack.index('Redux') +1, 'Python')
full_stack.insert(full_stack.index('Redux' +2,'SQL'))





