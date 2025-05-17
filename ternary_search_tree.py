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
