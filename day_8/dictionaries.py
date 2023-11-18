#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
#creating an empty dictionary
dog ={}
dog = {
    'key_name':'Bosco',
    'key_age' :12,
    'key_breed' :'German',
    'key_legs':4,
    'key_color' :'Black'
    }
Student = {
    'first_name':'Kelio',
    'last_name': 'Kerubo',
    'gender' :'femal',
    'age' : 23,
    'marital_status' : 'single',
    'Skills' :['Java','Python','JavaScript'],
    'country' :'Kenya'
}
Student_length = len(Student)
print(Student_length)
Skills = Student['Skills']
Skills_type = type(Skills)
print(Skills_type)
Skills.extend['SQL','PHP'] #adding items to skills key
keys_list =list(Student.keys)
values_list = list(Student.value)
dict_to_tuples =list(Student.items())#change dictionary to list of tuples using items()method
del Student['marital_status'] #deleting one item from dictionart
del dog #deleting one dictionary
print(Student)
