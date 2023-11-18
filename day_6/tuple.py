#A tuple is a collection of different data types which is ordered and unchangeable (immutable).
#creating an empty tuple
empty_tuple = () #creating an empty tuple
brothers =['Emmanuel' ,['Enock']]
sisters= ['Diana', 'Faith']
Siblings = sisters+brothers
print(Siblings)
print(len(Siblings))
family_members =('Calvin' , 'Alice') +Siblings #modifying 
print(family_members)

#EXERCISE_2
father ,mother, *Siblings = family_members #unpacking siblings from family_members

fruits =['Mango','Orange','Apple']
vegetables = ['Skuma','Sage','Cabbage']
animals_products = ['Cheese','butter','pork']
food_stuff_tp = fruits+vegetables+animals_products
print(food_stuff_tp)

food_stuff_tp = list(food_stuff_tp) #changing food_stuff_tp to a list
middle_item =food_stuff_tp[1:-1]
#slicing out the first three and last three
first_three = food_stuff_tp[:3]
last_three = food_stuff_tp[-3:]

del food_stuff_tp #delete the food_stuff_tp
