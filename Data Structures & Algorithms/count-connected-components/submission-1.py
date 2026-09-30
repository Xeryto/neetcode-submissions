class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        visited = set()

        def bfs(i):
            q = deque([i])

            while q:
                cur = q.popleft()
                visited.add(cur)

                for neigh in adj[cur]:
                    if not neigh in visited:
                        q.append(neigh)
        
        ans = 0
        for i, _ in edges:
            if not i in visited:
                bfs(i)
                ans+=1
            
        for i in range(n):
            if not i in visited:
                ans+=1
        
        return ans