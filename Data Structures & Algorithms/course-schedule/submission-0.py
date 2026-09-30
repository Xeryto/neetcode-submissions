class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = defaultdict(list)

        for a,b in prerequisites:
            indegree[b]+=1
            adj[a].append(b)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            cur = q.popleft()
            count+=1
            for i in adj[cur]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
        
        return count == numCourses
