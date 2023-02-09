import random
from words import words_list


def get_word():
    word = random.choice(words_list)
    return word.lower()


def play(word):
    word_completion = '_' * len(word)
    tries = 10
    guessed_letters = []
    guessed_words = []
    print('Welcome, lets play hangman!')
    print(word_completion)
    while tries > 0:
        word_completion = ''
        tries -= 1
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
        if len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print(f'yes you got it, the word is {guess}')
                break
            else:
                print(f'no that was not the right word {guess}')
                guessed_words.append(guess)
        for letter in word:
            if letter in guessed_letters:
                word_completion += letter
            elif letter not in guessed_letters:
                word_completion += '_'
        print(f'{word_completion} \n you have {tries} left')
        if word_completion == word:
            print('you got it')
    if tries == 0 and word_completion is not word:
        print(f'Sorry, you have no more tires, the word was {word}')




play(get_word())
