class TreeNode:
    def __init__(self, end=False):
        self.end = end
        self.children = {}

    def search(self, word):
        cur = self

        for i, c in enumerate(word):
            if c == '.':
                #kick off search fior all children, if any are true return it
                result = False
                for letter, child in cur.children.items():
                    result = result or child.search(word[i+1:])
                return result

            elif c not in cur.children: 
                return False

            cur = cur.children[c]
        
        return cur.end


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()


    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]

        cur.end = True
        
    def search(self, word: str) -> bool:
        return self.root.search(word)
    


        
        