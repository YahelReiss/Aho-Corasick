from AhoCorasickAlgorithm import AhoCorasick

words1 = ["a", "abcd", "ab", "cd", "bdd", ""]
alphabet1 = ["a", "b", "c", "d"]
string1 = "abccbdd"

words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'melon', 'strawberry', 'peach', 'kiwi', 'blueberry', 'ban', ', ']
string = 'I like to eat banana and pineapple, but I don\'t like kiwi.'
alphabet = [' ', "'", ',', '.', 'I', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y']

if __name__ == '__main__':
    A = AhoCorasick(words, string, alphabet)
    A.build_failure_and_suffix_links()
    A.find_words_in_string()
    print(A.res)
