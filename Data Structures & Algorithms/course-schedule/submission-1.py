class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for u,v in prerequisites:
            indegree[u]+=1
            graph[v].append(u)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        processed = 0
        while q:
            course = q.popleft()
            processed+=1
            for neigh in graph[course]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return processed==numCourses
