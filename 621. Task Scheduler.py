import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)
        time = 0
        
        while heap:
            temp = []
            for i in range(n + 1):
                if heap:
                    freq = -heapq.heappop(heap)
                    temp.append(freq - 1)
            
            for freq in temp:
                if freq > 0:
                    heapq.heappush(heap, -freq)
                    
            if not heap:
                time += len(temp)
            else:
                time += n + 1
                
        return time
