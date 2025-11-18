#Exercises: Day 7

#Exercises: Level 1
"""
1. Find the length of the set it_companies
2. Add 'Twitter' to it_companies
3. Insert multiple IT companies at once to the set it_companies
4. Remove one of the companies from the set it_companies
5. What is the difference between remove and discard (skip)
"""
#Exercises: Level 2
"""
6. Join A and B
7. Find A intersection B
8. Is A subset of B
9. Are A and B disjoint sets
10. Join A with B and B with A(skip)
11. What is the symmetric difference between A and B
12. Delete the sets completely
"""
#Exercises: Level 3
"""
13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?(skip)
14. Explain the difference between the following data types: string, list, tuple and set(skip)
15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
"""
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ages = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
len_of_companies = len(it_companies)
print(it_companies)
#2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#3. Insert multiple IT companies at once to the set it_companies
it_companies_to_add = ["Socia","Freelanceyyy","Riot"]
it_companies.update(it_companies_to_add)
print(it_companies)
#4. Remove one of the companies from the set it_companies
it_companies.remove("Apple")
print(it_companies)
#6. Join A and B
joined = A.union(B)
print(joined)
#7. Find A intersection B
intersection = A.intersection(B)
print(intersection)
#8. Is A subset of B
subset = A.issubset(B)
print(subset)
#9. Are A and B disjoint sets
disjoint_sets = A.isdisjoint(B)
print(disjoint_sets)
#11. What is the symmetric difference between A and B
symmtric_diff = A.symmetric_difference(B)
print(symmtric_diff)
#12. Delete the sets completely
del it_companies
#15. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.lower().replace(".", "").split()  # normalize text
unique_words = set(words)

print(unique_words)
print("Number of unique words:", len(unique_words))

