class Node:
    def __init__(self, val):
        self.val = val
        self.transitions = {}
        self.is_terminal = False
        self.to_print = []
        self.suffix_link = None
        self.parent = None
        self.failure_link = {}

    def __str__(self):
        val = None
        if self.suffix_link is not None:
            val = self.suffix_link.val
        return str(self.val) + " " + str(self.is_terminal) + str(self.to_print) + str(val) + "\n"
