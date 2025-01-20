dictionary = {"Shan":"Buland Martaby Wala", "Set":"Collection of Words",
              "Work":"Kamm Karna", "Crypto":"Virtual Currency"}


print("Enter a word to find its meaning")
word = input()

print("Your Word is", word)

print("Meaning of", word, "is:")
print(dictionary.get(word))

print("\nOR")

print(dictionary[word])

# That's it!!
