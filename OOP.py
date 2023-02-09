from random import *
from words import words_list


guessed = False
guessed_letters = []
guessed_words = []

def get_word():
    word = choice(words_list)
    return word.lower()
def start_game(word):
    tries = 4
    word_completion = '_' * len(word)
    print(f'Welcome, lets play hangman! You have {tries}')
    print(word_completion)
    check_guess(word, tries)
def check_guess(word, tries):
    player_guess = input('Guess a word or letter: ')
    tries -=1
    if len(player_guess) == 1 and player_guess.isalpha():
        if player_guess in word:
            print(f'Yes, that letter {player_guess} is in the word')
        elif player_guess not in word:
            print(f'Sorry, that letter {player_guess} is not in the word')
    if len(player_guess) == len(word) and player_guess.isalpha():
        if player_guess == word:
            guessed_words.append(player_guess)
        elif player_guess != word:
            print(f'Sorry {player_guess} is not the word')
            guessed_words.append(player_guess)
    update_board(player_guess, word, tries)
def update_board(guess, word, tries):
    word_completion = ''
    if len(guess) == 1 and guess not in guessed_letters:
        guessed_letters.append(guess)
    for char in word:
        if char in guessed_letters:
            word_completion += char
        else:
            word_completion += '_'
    if guess == word:
        word_completion = word
    check_if_game_over(word_completion, word, tries)


def check_if_game_over(word_completion, word, tries):
    if word_completion == word and tries >= 0:
        print(f'You won, the word was {word}')
        guessed = True
        return guessed
    elif word_completion != word and tries >=0:
        print(f'{word_completion} you have {tries} left')
        check_guess(word, tries)
    else:
        print(f'You are out of tries, the word was {word}')


start_game(get_word())




