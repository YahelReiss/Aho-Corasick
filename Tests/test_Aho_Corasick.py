import unittest
from AhoCorasickAlgorithm import AhoCorasick


class MyTestCase(unittest.TestCase):

    def test_empty_word_bank(self):
        words = []
        string = "abc"
        alphabet = ["a", "b", "c"]
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(A.res, [])

    def test_empty_string(self):
        words = ["a", "b", "c"]
        string = ""
        alphabet = ["a", "b", "c"]
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(A.res, [])

    def test_full_sentence(self):
        words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'melon', 'strawberry', 'peach', 'kiwi', 'blueberry',
                 'ban', ', ']
        string = 'I like to eat banana and pineapple, but I don\'t like kiwi.'
        alphabet = [' ', "'", ',', '.', 'I', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p',
                    'r', 's', 't', 'u', 'w', 'y']
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {'banana', 'pineapple', 'kiwi', 'ban', ', ', 'apple'})

    def test_case_sensitivity(self):
        words = ["Apple", "banana", "Pineapple", "KiWi"]
        string = "I like to eat banana and Pineapple, but I don't like KiWi."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {'banana', 'Pineapple', 'KiWi'})

    def test_overlapping_words(self):
        words = ["apple", "ppl"]
        string = "apples"
        alphabet = list(set(string))  # Assuming string characters form the alphabet
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {'apple', 'ppl'})

    def test_repeated_words_in_word_bank(self):
        words = ["apple", "banana", "apple", "banana", "apple"]
        string = "I like to eat apples and bananas, but I prefer kiwi."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        # Assert that each occurrence of the word is found
        self.assertEqual(set(A.res), {'apple', 'banana'})

    def test_repeated_words_in_string(self):
        words = ["apple", "banana"]
        string = "I like to eat apples, apples, apples, and bananas, bananas, bananas."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {'apple', 'banana'})

    def test_special_characters_in_word_bank(self):
        words = ["apple!", "banana?", "pineapple,", "kiwi.", "."]
        string = "I like to eat apple! and banana? and pineapple, but not kiwi."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {'apple!', 'banana?', 'pineapple,', 'kiwi.', "."})

    def test_special_characters_in_string(self):
        words = ["apple", "banana", "pineapple", "kiwi"]
        string = "I like to eat apple! and banana? and pineapple, but not kiwi."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        # Assert that each word is found, including those with special characters
        self.assertEqual(set(A.res), {'apple', 'banana', 'pineapple', 'kiwi'})

    def test_long_words(self):
        # Generate a long word by repeating a short word multiple times
        long_word = "aaaaaaaaaaaaaaaaaaaa"
        words = ["aaaaaaaaaaaaaaaaaaaa", "banana", "kiwi"]
        string = "I like to eat " + long_word + " and banana, but not kiwi."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        # Assert that the long word is found
        self.assertEqual(set(A.res), {"aaaaaaaaaaaaaaaaaaaa", "banana", "kiwi"})


if __name__ == '__main__':
    unittest.main()
