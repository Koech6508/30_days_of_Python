#Module is a file which contains a set of codes or functions which can be introduced into an application

# a function which generates a six digit/character random_user_id
import random
def random_user_id():
 return''.join(random.choice('0123456789abcdef')for _ in range(6))
print(random_user_id())

#Modifying the previous task. Declaring a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
  num_chars =int(input('Enter the number of characters: '))
  num_ids = int(input("Enter the number of IDs to generate: "))

  for _ in range(num_ids):
    user_id = ''.join(random.choice('0123456789abdcdef') for _ in range(num_chars))
    print(user_id)
user_id_gen_by_user()

#function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return f"(rgb{r},{g},{b})"
print(rgb_color_gen())

#a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
def list_of_hexa_colors(num_colors):
   return ['#' + ''.join(random.choice('0123456789abcdef') for _ in range(6)) for _ in range(num_colors)]
colors = list_of_hexa_colors(5)
print(colors)

#a function list_of_rgb_colors which returns any number of RGB colors in an array.
num_colors = ['red','blue','green']
def list_of_rgb_colors():
  return [rgb_color_gen() for _ in range(num_colors)]
print(list_of_rgb_colors())

#a function generate_colors which can generate any number of hexa or rgb colors.
def list_of_rgb_colors(num_colors):
  return [rgb_color_gen() for _ in range(num_colors)]

def generate_colors(color_type, num_colors):
  if color_type =='hexa':
   return list_of_hexa_colors(num_colors)
  elif color_type == 'rgb':
    return list_of_rgb_colors(num_colors)
  else :
    return[]
  
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))

#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

#a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
  return random.sample(range(10),7)

print(shuffle_list([1,2,3,4,5,6,7]))
print(unique_random_numbers())
