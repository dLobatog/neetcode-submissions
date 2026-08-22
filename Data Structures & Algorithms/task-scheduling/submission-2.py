class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        available = list(counter.values())
        heapq.heapify_max(available)

        # (ready time, remaining count)
        cooldown = deque()
        time = 0 

        while available or cooldown:
            while cooldown and cooldown[0][0] <= time:
                _, count = cooldown.popleft()
                heapq.heappush_max(available, count)
            
            if available:
                remaining = heapq.heappop_max(available)
                remaining -= 1
                if remaining > 0: 
                    cooldown.append((time + n + 1, remaining))


            time += 1

        return time
