import re
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


with open("pg10.txt","r") as f1:
    content1=f1.read()

with open("pg35997.txt","r") as f2:
    content2=f2.read()

content=content1+content2
lowercase_content=content.lower()

print("Task 1:")
tokens=word_tokenize(lowercase_content)
words=[i for i in tokens if not re.match(r'^[^\w\s]+$', i)]
with open("task_1.txt","w") as task_1:
    for i in words:
        print(f"{i}: {len(i)}",file=task_1)
print("Output written in task_1.txt file\n")

print("Task 2:")
lengths={}
for i in words:
    length=len(i)
    if length in lengths:
        lengths[length]+=1
    else:
        lengths[length]=1
sorted_lengths=dict(sorted(lengths.items()))
for i in sorted_lengths:
    print(f"Words with length of {i}: {sorted_lengths[i]}")
print()

print("Task 3:")
words_without_numbers=[i for i in tokens if i.isalpha()]
min_length=min(lengths.keys())
shortest_words=[i for i in words_without_numbers if len(i)==min_length]
unique_words=set(shortest_words)
print(f"Shortest word length: {min_length}")
print(f"Shortest words: {sorted(unique_words)}")
print(f"Total occurrences: {len(shortest_words)}")
shortest_freq={}
for i in shortest_words:
    if i in shortest_freq:
        shortest_freq[i]+=1
    else:
        shortest_freq[i]=1
print("Frequency of each shortest word:")
for word in sorted(shortest_freq.keys()):
    print(f"'{word}': {shortest_freq[word]:,} times")
print("Comments written in report.md file\n")

print("Task 4:")
sorted_lengths=dict(sorted(lengths.items()))
length=list(sorted_lengths.keys())
freq=list(sorted_lengths.values())
plt.plot(length,freq, marker='o')
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.title("Task 4")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]) 
plt.show()
print("Output in graph\n")

print("Task 5:")
log_length=np.log(length)
log_freq=np.log(freq)
plt.plot(log_length,log_freq, marker='o')
plt.xlabel("Log(Length)")
plt.ylabel("Log(Frequency)")
plt.title("Task 5")
plt.show()
print("Output in graph\n")

print("Task 6:")
x_array=np.array(length)
y_array=np.array(freq)
mean_x=np.mean(x_array)
mean_y=np.mean(y_array)
numerator=np.sum((x_array-mean_x)*(y_array-mean_y))
denominator=np.sqrt(np.sum((x_array-mean_x)**2)*np.sum((y_array-mean_y)**2))
print(f"Pearson Correlation: {numerator/denominator}\n")

print("Task 7:")
print("Short note written in report.md file")