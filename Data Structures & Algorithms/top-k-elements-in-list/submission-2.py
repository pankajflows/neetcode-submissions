class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        class Holder:
            def __init__(self, number, count=1):
                self.number = number
                self.count = count

            def __lt__(self, other):
                return self.count < other.count

        counter = defaultdict(int)
        for n in nums:
            counter[n] -= 1

        bank = list()
        for key,v in counter.items():
            bank.append(Holder(key,v))

        heapq.heapify(bank)

        ans = list()
        # print(bank)
        for n in range(k):
            # print("n", n)
            if bank:
                ans.append(heapq.heappop(bank).number)

        return ans

        