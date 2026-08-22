class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # (task_x, 0)
        # continue enqueing, while keeping track of "index"
        # next time we find task_x, we compute (index - queue[1]) 
        #  -----
        #.  - if >= n, continue enqueuing
        #.  - if <  n, stop enqueuing task_x. continue with other tasks? 
        #. -----
        #  priority queue? 
        #.   (task, prio i)
        #. if we counted the 26 tasks frequency we would have
        #.  { X: 2, Y: 2... }
        #. we could iterate this, and always be getting the most frequent task
        #. once we process the most frequent, we ensure
        # 2 heaps
        # heap for cooldown
        # heap for frequency 
        # we pull max frequency
        # then we put it on cooldown 
        # at the beginning of each cycle (until both heaps are empty) we first check cooldown, then we check max frequency
        # we always check they are < n
        # if neither condition is true, counter += 1

        counter = 0
        cooldown_h, freq_h = [], []
        heapq.heapify_max(freq_h)
        heapq.heapify(cooldown_h)
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t)-ord('A')] += 1

        for i in range(len(frequencies)):
            if frequencies[i] != 0:
                heapq.heappush_max(freq_h, (frequencies[i], -n-1, i)) # pushing the count
        
        while freq_h or cooldown_h:
            # print(freq_h, cooldown_h, counter)
            while cooldown_h and cooldown_h[0][0] <= counter:
                available_again, frequency, task = heapq.heappop(cooldown_h)
                heapq.heappush_max(freq_h, (frequency, available_again, task))

            if freq_h:
                frequency, last_push, task = heapq.heappop_max(freq_h)

                if frequency > 1:
                    heapq.heappush(cooldown_h, (counter + n + 1, frequency-1, task))

            counter += 1

        return counter
                

