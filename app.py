import random
from words import words_list


def get_word():
    word = random.choice(words_list)
    return word.lower()


def play(word):
    word_completion = '_ ' * len(word)
    guessed = False
    tries = 6
    guessed_letters = []
    word_as_list = []
    print('Welcome, lets play hangman!')
    print(word_completion)
    while guessed == False and tries > 0:
        word_completion = ''
        guess = input('guess a letter: ').lower()
        # check for only one letter and that it is a letter
        if len(guess) == 1 and guess.isalpha():
            # check if already made that guess
            if guess in guessed_letters:
                print(f'You already made that guess {guess}')
            # check if guess is in the word
            elif guess not in word:
                print(f'Sorry there is no {guess}')
                guessed_letters += guess
            else:
                print(f'Yes, there is a/an {guess}')
                guessed_letters += guess
        for letter in word:
            if letter in guessed_letters:
                word_completion += letter
            elif letter not in guessed_letters:
                word_completion += '_'
        tries -= 1
        print(word_completion, word)






play(get_word())
