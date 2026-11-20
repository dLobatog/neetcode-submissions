class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # tasks contain 0 to n 
        # [[enqueueTime, processingTime]....]
        # available to process at enqueueTime
        # will take processingTime to finish processing
        # 1 task at a time
        # if cpu is idle and tasks are available, choose shortest processing time
        #.  - min heap based on processing time + index?
        # once processing, must continue until stopping.
        # cpu can finish a task start a new one instantly

        # [1,4], [3,3], [2,1]
        pending = []
        for i, (enqueue, processing) in enumerate(tasks):
            heapq.heappush(pending, (enqueue, processing, i))

        ready = []
        order = []
        t = 0
        while pending or ready:
            if not ready:
                t = max(t, pending[0][0])

            while pending and pending[0][0] <= t:
                _, procTime, i = heapq.heappop(pending)
                heapq.heappush(ready, (procTime, i))

            
            procTime, i = heapq.heappop(ready)
            t += procTime
            order.append(i)

        return order