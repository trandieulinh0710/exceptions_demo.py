counts = dict()
text = input("Text: ")

parts = text.split()
parts.sort()
for word in parts:
    number_of_words = counts.get(word, 0)
    counts[word] = number_of_words + 1

for key in list(counts.keys()):
    print(f"{key} : {counts[key]}")
