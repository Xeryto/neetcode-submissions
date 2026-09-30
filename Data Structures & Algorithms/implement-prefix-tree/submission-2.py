class Node:
    def __init__(self):
        self.children = [-1]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.head = Node()
        return

    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if cur.children[ord(ch)-ord('a')] == -1:
                node = Node()
                cur.children[ord(ch)-ord('a')] = node
                cur = node
            else:
                cur = cur.children[ord(ch)-ord('a')]
        
        cur.endOfWord = True
        return

    def search(self, word: str) -> bool:
        cur = self.head
        for ch in word:
            if cur.children[ord(ch)-ord('a')] == -1:
                return False
            else:
                cur = cur.children[ord(ch)-ord('a')]
            
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for ch in prefix:
            if cur.children[ord(ch)-ord('a')] == -1:
                return False
            else:
                cur = cur.children[ord(ch)-ord('a')]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)