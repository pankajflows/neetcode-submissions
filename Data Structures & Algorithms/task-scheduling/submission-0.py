class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequencies of each task
        alpha_count = Counter(tasks)
        
        # Max-heap to always pick the most frequent available task
        # We only need the negative frequency; the character itself isn't strictly needed for sorting
        heap = [-v for v in alpha_count.values()]
        heapq.heapify(heap)

        # Queue stores pairs of (remaining_negative_frequency, time_it_becomes_available)
        queue = deque()
        global_time = 0

        while heap or queue:
            global_time += 1

            if heap:
                # Pop the highest frequency task available
                freq = heapq.heappop(heap)
                freq += 1  # Since it's negative, adding 1 brings it closer to 0
                
                # If there are still instances of this task left, put it in the cooldown queue
                if freq < 0:
                    queue.append((freq, global_time + n))
            else:
                # If heap is empty, the CPU is IDLE. 
                # We could just let global_time tick by 1, or fast-forward time to optimize.
                pass

            # Check if any tasks in the queue have completed their cooldown
            if queue and queue[0][1] == global_time:
                ready_freq, _ = queue.popleft()
                heapq.heappush(heap, ready_freq)

        return global_time









































        # while queue or heap:
        #     if not heap:
        #         if queue[0][2] <= time:
        #             triplet = queue.popleft()
        #             time += triplet[2]
        #             triplet[0] -= 1
        #             triplet[2] = n + time + 1
        #             if triplet[0] < 0:
        #                 heapq.heappush(heap, triplet)
                    
        #     else:
        #         time += 1
        #         triplet = heapq.heappop(heap)
        #         triplet[0] += 1
        #         triplet[2] = n + time
        #         if triplet[0] < 0:
        #             queue.append(triplet)

        # return time


            

        

        

        


        