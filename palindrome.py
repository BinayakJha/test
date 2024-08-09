# palindrome
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. Allowances may be made for adjustments to capital letters, punctuation, and word dividers. Examples in

# with this one from palindrome.py:

# -*- coding: utf-8 -*-

def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    return word == word[::-1]

