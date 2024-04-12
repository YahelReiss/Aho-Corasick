from Trie import Trie
from queue import Queue
from AhoCorasickAlgorithm import AhoCorasick


words = ["a", "abcd", "ab", "cd", "bdd", ""]
alphabet = ["a", "b", "c", "d"]
string = "abccbdd"

words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'melon', 'strawberry', 'peach', 'kiwi', 'blueberry']
string = 'I like to eat banana and pineapple, but I don\'t like kiwi.'
alphabet = [' ', "'", ',', '.', 'I', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']

if __name__ == '__main__':
    A = AhoCorasick(words, string, alphabet)
    A.build_failure_and_suffix_links()
    A.find_words_in_string()
    #
    # t = Trie(words, alphabet)
    # t.build_trie()
    # t.print_trie()
