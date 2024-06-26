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
        long_word = "aaaaaaaaaaa"
        words = [long_word, "banana", "kiwi"]
        string = "I like to eat " + long_word + " and banana, but not kiwi."
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        # Assert that the long word is found
        self.assertEqual(set(A.res), {"aaaaaaaaaaa", "banana", "kiwi"})

    def test_many_words(self):
        words = ["a", "aa", "aaa", "abbb", "aba", "abcdefg", "abcde", "banana", "kiwi"]
        string = "bananananaababababbbbbbbbabcdef"
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {"a", "aa", "abbb", "aba", "abcde", "banana"})

    def test_recursively_overlapping_words(self):
        words = ["a", "ba", "cbad"]
        string = "cba"
        alphabet = list(set(string)) + list(set(''.join(words)))
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        A.find_words_in_string()
        self.assertEqual(set(A.res), {"ba", "a"})


    def test_time(self):
        import time

        words = ["a", "b", "d", "e", "ab", "ad", "ae", "aa", "bd", "be", "bb", "ba", "da", "db", "dd", "de",
                 "ea", "eb", "ed", "ee", "aaa", "aab", "aad", "aae", "aba", "abb", "abd",
                 "abe", "ada", "adb", "add", "ade", "aea", "aeb", "aed", "aee", "baa", "bab", "bad", "bae", "bba",
                 "bbb", "bbd", "bbe", "bda", "bdb", "bdd", "bde", "bea", "beb", "bed", "bee", "daa", "dab", "dad",
                 "dae", "dba", "dbb", "dbd", "dbe", "dda", "ddb", "ddd", "dde", "dea", "deb", "ded", "dee", "eaa",
                 "eab", "ead", "eae", "eba", "ebb", "ebd", "ebe", "eda", "edb", "edd", "ede", "eea", "eeb", "eed", "eee"
                 ]
        string = "ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc" * 1000000 + "abde"
        alphabet = list(set(string)) + list(set(''.join(words)))

        # Measure runtime of the Aho-Corasick algorithm
        start_time = time.time()
        A = AhoCorasick(words, string, alphabet)
        A.build_failure_and_suffix_links()
        for _ in range(1):
            A.find_words_in_string()
        aho_corasick_runtime = time.time() - start_time

        # Measure runtime of the naive algorithm
        start_time = time.time()
        for _ in range(1):
            res = []
            for word in words:
                if word in string:
                    res.append(word)
        naive_algorithm_runtime = time.time() - start_time
        print(naive_algorithm_runtime)
        print(aho_corasick_runtime)


        start_time = time.time()
        res = []
        for word in words:
            word_length = len(word)
            for i in range(len(string) - word_length + 1):
                substring = string[i:i + word_length]
                if substring == word:
                    res.append(word)
                    break  # If the word is found, no need to continue searching
        naive_algorithm_runtime_python_implementation = time.time() - start_time
        print(naive_algorithm_runtime_python_implementation)


        # Assert that the runtime of Aho-Corasick is faster than the naive algorithm
        self.assertLess(aho_corasick_runtime, naive_algorithm_runtime_python_implementation)
        self.assertEqual(set(A.res), set(res))


if __name__ == '__main__':
    unittest.main()
