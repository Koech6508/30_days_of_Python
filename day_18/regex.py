#A regular expression or RegEx is a special text string that helps to find patterns in data
#the most frequent word in the following paragraph
from collections import Counter
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.split() #converting paragraphs into words
word_counts = Counter(words) #counts the frequency of each word
most_frequent_word = word_counts.most_common(1)[0][0]#finds the most frequent word
print('The most frequent word is:',most_frequent_word)

#Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) 
sorted_points = sorted(map(int,points))#converting points to integers
distance = sorted_points[-1] - sorted_points[0]
print("Distance between furthest particles is: ",distance)

#Write a pattern which identifies if a string is a valid python variable
import re
def is_valid_variable(variable):
    pattern = re.compile(r'^[a-zA-Z_]\w*$')
    return bool(pattern.match(variable))
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

#Clean the following text. After cleaning, count three most frequent words in the string.
import re
from collections import Counter

def clean_text(text):
    cleaned_text = re.sub(r'[^a-zA-Z\s]','',text)
    return cleaned_text.lower()
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

word_counts = Counter(cleaned_text.split())
most_frequent_words = word_counts.most_common(3)
print('Three most frequent words are:' , most_frequent_words)