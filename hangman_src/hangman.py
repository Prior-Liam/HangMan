# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hangman.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Prior-Liam <LiamPrior44@gmail.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/06 16:14:59 by Prior-Liam        #+#    #+#              #
#    Updated: 2024/05/07 17:41:05 by Prior-Liam       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

class Choose_word:#done
    def __init__(self):
        self.word_list = ["python", "programming", "hangman", "computer", "keyboard", "developer", "learning"]
        self.word = str(random.choice(self.word_list))
    def Get_word(self):
        return self.word

class Make_display:#done
    def __init__(self):
        self.displayed_word = ""
    def display_word(self, word, guessed_letters):
        self.displayed_word = ""
        for letter in word:
            if letter in guessed_letters:
                self.displayed_word += letter + " "
            else:
                self.displayed_word += "_ "
        return self.displayed_word.strip()

class Hangman_game():
    def __init__(self, chosen_word):
        self.word_to_guess = chosen_word
        self.guessed_letters = []

    def get_word_to_guess(self):#done
        return self.word_to_guess

    def get_guessed_letters(self):#done
        return self.guessed_letters

    def make_guess(self, guess):#done
        if len(guess) != 1 or not guess.isalpha():
            return -1
        if guess in self.guessed_letters:
            return 0
        else:
            self.guessed_letters.append(guess)
            return 1
            
    def check_guess(self):#done
        if self.guessed_letters[-1] in self.word_to_guess:#done
            return 1
        return 0
        
    def check_guessed_letters(self, guessed_display_letters):#done
        if "_" not in guessed_display_letters:
            return 1
        return 0

    def check_guessed_word(self, guessed_word):#done
        if str(guessed_word) == self.word_to_guess:
            return 1
        return 0
    
    def give_hint(self):
        return self.word_to_guess[0]

    def reset_game(self):
        self.word_to_guess = Choose_word().Get_word()  # Get a new random word
        self.guessed_letters = [] 
        return 1
