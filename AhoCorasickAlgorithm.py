from Trie import Trie
from Node import Node
from queue import Queue


class AhoCorasick:
    def __init__(self, bank_words, string, alphabet):
        self.t = Trie(bank_words, alphabet)
        self.t.build_trie()
        self.string = string
        self.alphabet = alphabet
        self.res = []

    def build_failure_and_suffix_links(self):
        tree = self.t
        root = tree.root
        q = Queue()
        q.put(root)
        parent = Node("dummy")
        parent.transitions = {char: root for char in self.alphabet}
        parent.transitions[""] = parent
        parent.suffix_link = parent
        root.parent = parent
        while not q.empty():
            curr = q.get()
            parent = curr.parent
            curr.suffix_link = parent.suffix_link.transitions[curr.val] if curr.val in parent.suffix_link.transitions\
                else parent.suffix_link.failure_link[curr.val]
            for char in self.alphabet:
                if char not in curr.transitions or (curr == root and char in tree.pseudo_transitions):
                    curr.failure_link[char] = curr.suffix_link.transitions[char] \
                        if char in curr.suffix_link.transitions else curr.suffix_link.failure_link[char]
                else:
                    q.put(curr.transitions[char])

    def find_words_in_string(self):
        curr = self.t.root
        if curr.is_terminal:
            self.res.append(curr.to_print[0])
        for i, char in enumerate(self.string):
            if char in curr.transitions:
                curr = curr.transitions[char]
            else:
                curr = curr.failure_link[char]
            if curr.is_terminal:
                self.res.append(curr.to_print[0])
            if curr.suffix_link.is_terminal:
                self.res.append(curr.suffix_link.to_print[0])

    def print_trie(self, num):
        self.t.recursive_print(self.t.root, num)
