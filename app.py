import random
from words import words_list


def get_word():
    word = random.choice(words_list)
    return word.lower()


def play(word):
    word_completion = '_ ' * len(word)
    guessed = False
    tries = 3
    guessed_letters = []
    print('Welcome, lets play hangman!')
    print(word_completion)
    while guessed == False and tries > 0:
        letter_guessed = input('guess a letter: ').lower()
        # check for only one letter and that it is a letter
        if len(letter_guessed) == 1 and letter_guessed.isalpha():
            guessed_letters += letter_guessed
            word_completion = ''
            for letter in word:
                for item in guessed_letters:
                    print(letter, item)
        tries -= 1


play(get_word())
