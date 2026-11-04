class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for i in range(numCourses)]

        adj = defaultdict(list)

        for a,b in prerequisites:
            indegree[a]+=1
            adj[b].append(a)
        
        q = []
        for course, count in enumerate(indegree):
            if count == 0:
                q.append(course)

        ans = []
        
        while q:
            course = q.pop(0)
            ans.append(course)

            for dep in adj[course]:
                indegree[dep]-=1
                if indegree[dep] == 0:
                    q.append(dep)
        
        return [] if indegree.count(0) != numCourses else ans