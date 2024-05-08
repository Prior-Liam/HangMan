# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hangman_tests.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Prior-Liam <LiamPrior44@gmail.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/07 09:57:33 by Prior-Liam        #+#    #+#              #
#    Updated: 2024/05/07 17:41:00 by Prior-Liam       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import unittest
from hangman_src.hangman import Choose_word, Make_display, Hangman_game

class TestHangmanGame(unittest.TestCase):

    def setUp(self):
        self.word_selector = Choose_word()
        self.game = Hangman_game("programming")
        self.display = Make_display()

    def test_chosen_word(self):
        # self.word_selector.Get_word()
        self.assertTrue(self.word_selector.Get_word() in self.word_selector.word_list)
        self.assertTrue(isinstance(self.game.get_word_to_guess(), str))
        self.assertTrue(self.game.get_word_to_guess() in self.word_selector.word_list)

    def test_display_word(self):
        test_word = "programming"
        guessed_letters = {'p', 'r', 'g'}
        displayed_word = self.display.display_word(test_word, guessed_letters)
        self.assertEqual(displayed_word, "p r _ g r _ _ _ _ _ g")

    def test_game_class(self):
        self.assertEqual(self.game.make_guess('a'), 1)  # Valid guess
        self.assertEqual(self.game.check_guess(), 1)
        self.assertEqual(self.game.make_guess('a'), 0)  # Already guessed
        self.assertEqual(self.game.make_guess('123'), -1)  # Invalid guess
        self.assertEqual(self.game.make_guess('z'), 1)  # Invalid guess
        self.assertEqual(self.game.check_guess(), 0)
        self.assertEqual(self.game.check_guessed_letters(self.display.display_word(self.game.get_word_to_guess(), self.game.get_guessed_letters())), 0) #checks to see that its not done
        self.game.make_guess('p')
        self.game.make_guess('r')
        self.game.make_guess('o')
        self.game.make_guess('g')
        self.game.make_guess('m')
        self.game.make_guess('i')
        self.game.make_guess('n')
        self.assertEqual(self.game.check_guessed_letters(self.display.display_word(self.game.get_word_to_guess(), self.game.get_guessed_letters())), 1)

    def test_check_guessed_word(self):
        self.assertEqual(self.game.check_guessed_word("yeee"), 0)
        self.assertEqual(self.game.check_guessed_word(self.game.get_word_to_guess()), 1)  # Should be True

    def test_give_hint(self):
        self.assertEqual(self.game.give_hint(), "p")

    def test_reset_game(self):
        self.assertEqual(self.game.reset_game(), 1)
        self.assertEqual(self.game.get_guessed_letters(), [])
        self.assertTrue(self.game.get_word_to_guess() in self.word_selector.word_list)
#make a test where they win with the word python purely through letter guesses#1
#make a test where they win by choossing the guess word at the end#2
#make a test where they fail all guesses and final word guess
#make a test where i give them a hint and they pass
#make a test where the game is reset
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.word_selector = Choose_word()
        self.game = Hangman_game("python")
        self.display = Make_display()
    
    def test_win_by_letters(self):#1
        self.game.make_guess('p')
        self.game.make_guess('y')
        self.game.make_guess('t')
        self.game.make_guess('h')
        self.game.make_guess('o')
        result = self.game.make_guess('n')
        self.assertEqual(result, 1)
        self.assertEqual(self.game.check_guessed_letters(self.display.display_word(self.game.get_word_to_guess(), self.game.get_guessed_letters())), 1)
    
    def test_win_by_guess(self):#2
        self.game.make_guess('z')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('x')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('c')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('v')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('b')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('m')
        self.assertEqual(self.game.check_guess(), 0)#out of guesses
        self.assertEqual(self.game.check_guessed_word("python"), 1)
    
    def test_win_by_hint(self):#3
        self.game.make_guess(self.game.give_hint())
        self.assertEqual(self.game.check_guess(), 1)
        self.game.make_guess('x')
        self.game.make_guess('c')
        self.game.make_guess('v')
        self.game.make_guess('b')
        self.game.make_guess('m')
        self.assertEqual(self.game.check_guessed_word("python"), 1)
    def test_fail_all(self):#4
        self.game.make_guess('x')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('c')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('t')
        self.assertEqual(self.game.check_guess(), 1)#lil check
        self.game.make_guess('b')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('m')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('z')
        self.assertEqual(self.game.check_guess(), 0)
        self.assertEqual(self.game.check_guessed_word("yeee"), 0)

    def test_reset(self):#4
        self.game.make_guess('z')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('x')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('c')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('v')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('b')
        self.assertEqual(self.game.check_guess(), 0)
        self.game.make_guess('m')
        self.assertEqual(self.game.check_guess(), 0)#out of guesses
        self.assertEqual(self.game.check_guessed_word("python"), 1)
        self.assertEqual(self.game.reset_game(), 1)
        self.assertEqual(self.game.get_guessed_letters(), [])
        self.assertTrue(self.game.get_word_to_guess() in self.word_selector.word_list)
if __name__ == '__main__':
    unittest.main()
