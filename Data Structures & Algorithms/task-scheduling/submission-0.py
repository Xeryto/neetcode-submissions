class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26

        for task in tasks:
            freq[ord(task)-ord("A")]+=1
        
        heap = []

        for task in set(tasks):
            heapq.heappush(heap, (-1*freq[ord(task)-ord("A")],task))
        
        q = []

        timeout = [0]*26

        ans = 0
        while freq.count(0) != 26:
            if not heap:
                ans+=1
                for task in q:
                    timeout[ord(task)-ord("A")] -= 1
                
                while q and timeout[ord(q[0])-ord("A")] == 0:
                    if freq[ord(q[0])-ord("A")] > 0:
                        heapq.heappush(heap, (-1*freq[ord(q[0])-ord("A")],q.pop(0)))
                    else:
                        q.pop(0)
                continue
            else:
                ans+=1
                fr, el = heapq.heappop(heap)
                freq[ord(el)-ord("A")] -= 1
                timeout[ord(el)-ord("A")] = n
                for task in q:
                    timeout[ord(task)-ord("A")] -= 1
                
                while q and timeout[ord(q[0])-ord("A")] == 0:
                    if freq[ord(q[0])-ord("A")] > 0:
                        heapq.heappush(heap, (-1*freq[ord(q[0])-ord("A")],q.pop(0)))
                    else:
                        q.pop(0)

                q.append(el)
            
        
        return ans