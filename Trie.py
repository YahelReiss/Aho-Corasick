from Node import Node


class Trie:
    def __init__(self, words: list[str], alphabet):
        self.alphabet = alphabet
        self.words = words
        self.pseudo_transitions = []
        self.root: Node = Node("")
        self.root.failure_link = {char: self.root for char in alphabet}
        self.root.failure_link[""] = self.root
        self.root.suffix_link = self.root
        self.root.state = ""
        self.root.transitions[""] = self.root

    def build_trie(self):
        for word in self.words:
            if word == "":
                self.root.is_terminal = True
                break
            length = len(word)
            curr = self.root
            for i, char in enumerate(word):
                if char not in curr.transitions:
                    new_transition = Node(char)
                    new_transition.state = curr.state + char
                    new_transition.parent = curr
                    curr.transitions[char] = new_transition
                curr = curr.transitions[char]
                if i == length - 1:
                    curr.is_terminal = True
                    curr.to_print.append(curr.state)
        for char in self.alphabet:
            if char not in self.root.transitions:
                self.root.transitions[char] = self.root
                self.pseudo_transitions.append(char)

    def recursive_print(self, node, num=100):
        if num <= 0:
            return
        print(node)
        if node.transitions:
            kids = [child for child in node.transitions.values()]
            for kid in kids:
                self.recursive_print(kid, num - 1)

    def print_trie(self):
        self.recursive_print(self.root)
