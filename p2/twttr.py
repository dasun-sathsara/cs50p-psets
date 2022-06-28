vowels = [v for v in "a e i o u".split()]
vowels.extend([v.upper() for v in vowels])

user_word = input("Enter a word: ")
short_word = user_word

for vowel in vowels:
    short_word = short_word.replace(vowel, "")

print(short_word)
