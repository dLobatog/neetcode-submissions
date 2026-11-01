class Node:
    def __init__(self, isWord=False):
        self.children = {}
        self.isWord = isWord

class PrefixTree:

    def __init__(self):
        self.root = Node()
    

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char] 
            else:
                return False
        return current.isWord
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char] 
            else:
                return False
        return True
        
        