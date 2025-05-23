class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

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

    def search(self, word, exact=False):
        return self._search(self.root, word, 0, exact)

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

    def traverse(self):
        words = []
        self._traverse(self.root, '', words)
        return words

    def _traverse(self, node, prefix, result):
        if node is None:
            return

        self._traverse(node.left, prefix, result)

        if node.is_end:
            result.append(prefix + node.char)

        self._traverse(node.eq, prefix + node.char, result)
        self._traverse(node.right, prefix, result)

    def __len__(self):
        return len(self.traverse())

    def all_strings(self):
        return self.traverse()
