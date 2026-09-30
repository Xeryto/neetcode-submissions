class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words)-1):
            minLen = min(len(words[i]), len(words[i+1]))
            if len(words[i]) > len(words[i+1]) and words[i][:minLen] == words[i+1][:minLen]:
                return ""
            
            for j in range(minLen):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in adj[words[i][j]]:
                        adj[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]] +=1
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        ans = ""

        while q:
            cur = q.popleft()
            ans+=cur
            
            for neigh in adj[cur]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return ans if len(ans) == len(indegree) else ""