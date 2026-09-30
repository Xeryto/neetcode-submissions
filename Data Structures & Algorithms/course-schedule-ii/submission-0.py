class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        inorder = [0]*numCourses

        for a,b in prerequisites:
            adj[b].append(a)
            inorder[a] +=1
        
        q = deque()

        for i in range(numCourses):
            if inorder[i] == 0:
                q.append(i)
        ans = []
        count = 0
        while q:
            cur = q.popleft()
            count+=1
            ans.append(cur)

            for neigh in adj[cur]:
                inorder[neigh]-=1
                if inorder[neigh] == 0:
                    q.append(neigh)
        
        return ans if numCourses == count else []

        