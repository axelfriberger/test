
letters_1 = ["a", "p", "p", "l", "e", "p"]
words = "apple"
word = [letter for letter in words]
letters_fixed = [letter for letter in letters_1 if letter != "null"]

print(word)
print(letters_fixed)

word_2 = word
for letter in words:
    letters_fixed.remove(letter)
    word_2.remove(letter)




print(letters_fixed)
print(word_2)