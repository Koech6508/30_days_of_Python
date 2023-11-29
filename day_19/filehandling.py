#day is usually stored in different fileformats(.txt, .json, .xml, .csv, .tsv, .excel)
import re
import json
from collections import Counter
# Function to count lines and words in a text
def count_lines_and_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        lines = text.split('\n')
        words = re.findall(r'\b\w+\b', text)
        return len(lines), len(words)

# Function to find the most spoken languages
def most_spoken_languages(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)
        languages = Counter(country['languages'].split(', ') for country in data)
        return languages.most_common(n)

# Function to find the most populated countries
def most_populated_countries(filename, n):
    with open(filename, 'r') as file:
        data = json.load(file)
        countries = [{'country': country['name'], 'population': country['population']} for country in data]
        return sorted(countries, key=lambda x: x['population'], reverse=True)[:n]

# Function to extract incoming email addresses
def extract_email_addresses(filename):
    with open(filename, 'r') as file:
        text = file.read()
        email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return email_addresses

# Function to find the most common words in English
def find_most_common_words(filename, n):
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        common_words = Counter(words).most_common(n)
        return common_words

# Function to find most frequent words in a given text
def find_most_frequent_words(text, n):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return Counter(words).most_common(n)

# Function to check text similarity
def check_text_similarity(text1, text2):
    words1 = set(find_most_frequent_words(text1, 10))
    words2 = set(find_most_frequent_words(text2, 10))
    similarity = len(words1.intersection(words2)) / len(words1.union(words2)) * 100
    return similarity

# Function to remove stop words
def remove_stop_words(text, stop_words):
    words = re.findall(r'\b\w+\b', text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Function to clean text
def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

# Read stop words from file
with open('./data/stop_words.txt', 'r') as stop_words_file:
    stop_words = stop_words_file.read().split('\n')

# Reading text files
obama_speech = open('./data/obama_speech.txt', 'r').read()
michelle_obama_speech = open('./data/michelle_obama_speech.txt', 'r').read()
donald_speech = open('./data/donald_speech.txt', 'r').read()
melina_trump_speech = open('./data/melina_trump_speech.txt', 'r').read()

# a) Count number of lines and words in Obama's speech
lines, words = count_lines_and_words('./data/obama_speech.txt')
print(f"Obama's Speech: Lines - {lines}, Words - {words}")

# b) Count number of lines and words in Michelle's speech
lines, words = count_lines_and_words('./data/michelle_obama_speech.txt')
print(f"Michelle's Speech: Lines - {lines}, Words - {words}")

# c) Count number of lines and words in Donald's speech
lines, words = count_lines_and_words('./data/donald_speech.txt')
print(f"Donald's Speech: Lines - {lines}, Words - {words}")

# d) Count number of lines and words in Melina's speech
lines, words = count_lines_and_words('./data/melina_trump_speech.txt')
print(f"Melina's Speech: Lines - {lines}, Words - {words}")

# a) The ten most frequent words used in Obama's speech
most_frequent_words_obama = find_most_frequent_words(obama_speech, 10)
print("Obama's Speech: Most Frequent Words -", most_frequent_words_obama)

# b) The ten most frequent words used in Michelle's speech
most_frequent_words_michelle = find_most_frequent_words(michelle_obama_speech, 10)
print("Michelle's Speech: Most Frequent Words -", most_frequent_words_michelle)

# c) The ten most frequent words used in Trump's speech
most_frequent_words_trump = find_most_frequent_words(donald_speech, 10)
print("Trump's Speech: Most Frequent Words -", most_frequent_words_trump)

# d) The ten most frequent words used in Melina's speech
most_frequent_words_melina = find_most_frequent_words(melina_trump_speech, 10)
print("Melina's Speech: Most Frequent Words -", most_frequent_words_melina)