import pandas

nato_p_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in nato_p_alphabet.iterrows()}

word_to_spell = input("Give me a word: \n")

letters = [letter.capitalize() for letter in word_to_spell]

npa_word = [alphabet[letter] for letter in letters]

print(npa_word)