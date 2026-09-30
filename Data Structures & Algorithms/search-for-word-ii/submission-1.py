class Node():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie():
    def __init__(self):
        self.head = Node()
        return
    
    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.children:
                node = Node()
                cur.children[ch] = node
            cur = cur.children[ch]
        
        cur.endOfWord = True
        return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        maxlen = 0
        for word in words:
            maxlen = max(maxlen, len(word))
            trie.insert(word)

        ans = set()
        
        def dfs(i,j, word, cur):
            if (
    (i >= len(board))
    or (i < 0)
    or (j >= len(board[i]))
    or (j < 0)
    or (board[i][j] not in cur.children)
    or (len(word) + 1 > maxlen)
    or board[i][j] == "*"
):
                return
            
            

            node = cur.children[board[i][j]]
            word+=board[i][j]

            if node.endOfWord:
                ans.add(word)
            
            tmp = board[i][j]
            board[i][j] = '*'

            dfs(i+1, j, word, node)
            dfs(i-1, j, word, node)
            dfs(i, j+1, word, node)
            dfs(i, j-1, word, node)

            board[i][j] = tmp
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i,j, "", trie.head)
        
        return list(ans)