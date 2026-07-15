sentence = input("Enter a sentence: ")

words = sentence.lower().split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)