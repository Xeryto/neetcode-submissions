class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        adj = [set() for i in range(numCourses)]

        prereqs = [set() for i in range(numCourses)]

        for a,b in prerequisites:
            adj[a].add(b)
            indegree[b]+=1

        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            for neigh in adj[cur]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    q.append(neigh)
                prereqs[neigh].add(cur)
                prereqs[neigh].update(prereqs[cur])
        
        ans = []
        for u,v in queries:
            ans.append(u in prereqs[v])

        return ans
