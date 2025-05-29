# Node class for each character in the tree
class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False


# Main class for the Ternary Search Tree
# This implementation allows for insertion, searching, and traversal of words.
class TernarySearchTree:
    def __init__(self):
        self.root = None

    # Inserts a word into the Ternary Search Tree
    # If the word already exists, it will not be added again.
    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

    # Helper method to insert a word recursively
    # It traverses the tree based on character comparison and inserts the word.
    def _insert(self, node, word, index):
        char = word[index]
        if node is None:
            node = TSTNode(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                node.is_end = True
        return node

    # Searches for a word in the Ternary Search Tree
    # If exact is True, it will only return True if the word is exactly found.
    # If exact is False, returns True if word is found anywhere.
    def search(self, word, exact=False):
        return self._search(self.root, word, 0, exact)

    # Helper method to search for a word recursively
    # It traverses the tree based on character comparison.
    def _search(self, node, word, index, exact):
        if word == '':
            return not exact and node is not None

        if node is None:
            return False

        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index, exact)
        elif char > node.char:
            return self._search(node.right, word, index, exact)
        else:
            if index + 1 == len(word):
                return node.is_end if exact else True
        return self._search(node.eq, word, index + 1, exact)

    # Traverses the Ternary Search Tree and returns all words stored in it
    def traverse(self):
        words = []
        self._traverse(self.root, '', words)
        return words

    # Helper method to traverse the tree recursively
    def _traverse(self, node, prefix, result):
        if node is None:
            return

        self._traverse(node.left, prefix, result)

        if node.is_end:
            result.append(prefix + node.char)

        self._traverse(node.eq, prefix + node.char, result)
        self._traverse(node.right, prefix, result)

    # Returns the number of words in the tree
    def __len__(self):
        return len(self.traverse())

    # Returns all strings stored in the tree
    def all_strings(self):
        return self.traverse()
