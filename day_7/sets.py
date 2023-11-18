#Set is a collection of unordered and un-indexed distinct elements.
st = set()#creating an empty set
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('twitter')
it_companies.remove('IBM')
print(it_companies)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(A.intersection(B))# returns elements which a both on the list
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A
del B

age = [22, 19, 24, 25, 26, 24, 25, 24]
st =set(age)#convert list to set
print(len(st))
print(len(age))
diff =st.symmetric_difference(age)
print(diff)

sentence = "I am a teacher and I love to inspire and teach people"
unique_words =set(sentence.split())
print(unique_words)
print(len(unique_words))