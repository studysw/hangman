__author__ = 'user'

import unittest
import hangman

class hangmanTestCase(unittest.TestCase):

    #checkCorrectAnswer
    def test_checkCorrectAnswer (self):
        answer = hangman.checkCorrectAnswer("a, c, t", "cat")
        self.assertTrue(answer)

    