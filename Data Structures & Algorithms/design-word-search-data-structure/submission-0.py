class Node():
    def __init__(self):
        self.children = defaultdict(None)
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.head
        return self.searchDfs(word, cur)
    
    def searchDfs(self, word, node):
        cur = node
        for i,ch in enumerate(word):
            if ch == ".":
                flag = False
                for child in cur.children.values():
                    flag = flag | self.searchDfs(word[i+1:], child)
                return flag
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return cur.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)