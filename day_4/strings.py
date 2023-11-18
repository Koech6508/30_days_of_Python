challenge = 'Thirty'+ 'Days'+'Of'+ 'Python'
print(challenge)

strinf1 = 'Coding'+ 'For' + 'All'
print(strinf1)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print('Coding' in company)
print(company.replace("Coding" ,"python"))
print(company.replace("All","Everyone"))
print(company.split())
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))
print(company[0])
print(company[-1])
print(company[10])

print(''.join(word[0].upper() for word in 'Python For Everyone'.split()))
print(''.join(word[0] for word in 'Coding For All'.split()))
print(company.index('C'))
print(company.index('F'))
print(company.rfind('I'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(slice('because'))
print(company.startswith('Coding'))
print(company.endswith('coding'))

idea = '   Coding For All      '
print(idea.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libraries =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print("Name\t\tAge\tCountry\tCity\nDeborah\t250\tKenya\tNakuru")

radius = 10
area = 3.14*radius**2
print(f'The area of a circle with radius{radius}  is area{area} meters square.')
print(f'8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')