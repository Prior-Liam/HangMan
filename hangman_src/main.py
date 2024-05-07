# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Prior-Liam <LiamPrior44@gmail.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 09:57:30 by Prior-Liam        #+#    #+#              #
#    Updated: 2024/05/07 11:55:38 by Prior-Liam       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from hangman import Choose_word, Make_display, Hangman_game


if __name__ == "__main__":
    print("Welcome to Hangman!")
    word_selecter = Choose_word()
    game = Hangman_game(word_selecter.Get_word())
    print(word_selecter.Get_word())
    allow_long_shot = 1
    i = 0
    print("Try to guess the word.")
    display = Make_display()
    print(display.display_word(word_selecter.Get_word(), set("")))
    while (i < 6):
        guess = input("Enter a letter: ").lower()
        result = game.make_guess(guess)
        if (result == -1):
            print("Guess must be a single letter from the alphabet.")
        elif result == 0:
            print("You've already guessed that letter.")
        elif result == 1:
            if game.check_guess() == 1:
                print("Nice! Thats one of the letters!")
            else:
                print("Sorry that's not in the word!")
            print("You have", 6-(i+1), "chances left")
            i+=1
            print(display.display_word(game.get_word_to_guess(), game.get_guessed_letters()))
            if (game.check_guessed_letters(display.display_word(word_selecter.Get_word(),game.get_guessed_letters())) == 1):
                print("Congradulations, You Win!")
                allow_long_shot = 0
                break
    if (allow_long_shot == 1):
        guessed_word = input("Go ahead and try to guess the entire word now: ").lower()
        if game.check_guessed_word(guessed_word) == 1:
            print("Nice Work! You Win!")
        else:
            print("Better luck next time, you lose!")
    game.reset_game()
        
