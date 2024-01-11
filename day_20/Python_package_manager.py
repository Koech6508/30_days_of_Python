# Package is a Python module that can contain one or more modules or other packages, we do not have to write every utility program, instead we install packages and import them to our applications.
import requests
from collections import Counter
from bs4 import BeautifulSoup

# URL of Romeo and Juliet text on Gutenberg
romeo_and_juliet_url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(romeo_and_juliet_url)#send a get request to the url and get the response
html_content = response.text #extract html content from the response

# Use BeautifulSoup to parse HTML content and extract text
soup = BeautifulSoup(html_content,'html.parser')
text = soup.get_text()

words = text.split() #tokenizes the text into a list of words
words_count = Counter(words)#counts the occurence of each word on the list
most_frequent_words = words_count.most_common(10)
print('10 Most frequent words in Romeo and Juliet:', most_frequent_words)

#Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#the min, max, mean, median, standard deviation of cats' weight in metric units.the min, max, mean, median, standard deviation of cats' lifespan in years.
import requests
import numpy as np
import pandas as pd

# Defining the API URL for cat breeds
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api) #Sending a GET request to the cat breeds API to get the response
cats_data = response.json()## Parsing the JSON response into a Python dictionary

# Extracting weight and lifespan data into lists
weights = [float(cat['weight']['metric'].split()[0]) for cat in cats_data]
lifespans = [float(cat['life_span'].split()[0]) for cat in cats_data]

# Calculating statistics for weight and lifespan
weight_stats = {
    'min': np.min(weights),
    'max': np.max(weights),
    'mean': np.mean(weights),
    'median': np.median(weights),
    'std': np.std(weights)
}

lifespan_stats = {
    'min': np.min(lifespans),
    'max': np.max(lifespans),
    'mean': np.mean(lifespans),
    'median': np.median(lifespans),
    'std': np.std(lifespans),
}
print("Statistics on Cats' Weight (Metric Units):")
print(f"Minimum: {weight_stats['min']}")
print(f"Maximum: {weight_stats['max']}")
print(f"Mean: {weight_stats['mean']}")
print(f"Median: {weight_stats['median']}")
print(f"Standard Deviation: {weight_stats['std']}")

print("\nStatistics on Cats' Lifespan (Years):")
print(f"Minimum: {lifespan_stats['min']}")
print(f"Maximum: {lifespan_stats['max']}")
print(f"Mean: {lifespan_stats['mean']}")
print(f"Median: {lifespan_stats['median']}")
print(f"Standard Deviation: {lifespan_stats['std']}")