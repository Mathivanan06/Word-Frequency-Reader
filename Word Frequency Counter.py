frequency = {}
sentence = input("Enter a sentence:")

for word in sentence.split():
    frequency[word] = frequency.get(word, 0)+1

words = frequency.keys()
words = sorted(words)

for item in words:
    print(f"{item} = {frequency[item]}")
