import pytest

def disemvowel(string_):
    letters = list(string_)
    #  a, e, i, o, u,
    vowels = ['a', 'o', 'e', 'i', 'u']
    vowels_capital = [vowel.upper() for vowel in vowels]
    vowels_all = vowels + vowels_capital
    letters_no_vowels = [letter for letter in letters if letter not in vowels_all]
    string_ = "".join(letters_no_vowels)
    return string_

if __name__ == "__main__":
    string = 'This website is for losers LOL!'
    print(disemvowel(string))
