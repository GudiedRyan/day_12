import pandas

nato_p_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in nato_p_alphabet.iterrows()}

good_input = False

while good_input == False:
    word_to_spell = input("Give me a word: \n")

    try:
        letters = [letter.capitalize() for letter in word_to_spell]
        npa_word = [alphabet[letter] for letter in letters]
    except KeyError:
        print("Please do not use any non alphabetical characters.")
    
    else:
        good_input = True
print(npa_word)