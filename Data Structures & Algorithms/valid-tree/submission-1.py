class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(parent, i):
            print(parent,i, visited)
            if i in visited:
                return False
            visited.add(i)
            for b in adj[i]:
                if b != parent:
                    if not dfs(i,b):
                        return False
            
            return True

        if not dfs(-1,0):
            return False
        return len(visited) == n

