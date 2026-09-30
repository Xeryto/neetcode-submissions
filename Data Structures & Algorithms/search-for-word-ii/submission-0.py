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
        
        def dfs(i,j, visited, word, cur):
            if (
    (i >= len(board))
    or (i < 0)
    or (j >= len(board[i]))
    or (j < 0)
    or ((i, j) in visited)
    or (board[i][j] not in cur.children)
    or (len(word) + 1 > maxlen)
):
                return
            node = cur.children[board[i][j]]
            word+=board[i][j]
            visited.add((i,j))
            if node.endOfWord:
                ans.add(word)
            
            dfs(i+1, j, visited.copy(), word, node)
            dfs(i-1, j, visited.copy(), word, node)
            dfs(i, j+1, visited.copy(), word, node)
            dfs(i, j-1, visited.copy(), word, node)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i,j, set(), "", trie.head)
        
        return list(ans)