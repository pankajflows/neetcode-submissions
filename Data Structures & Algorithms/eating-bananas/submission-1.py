class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(n):
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / n)
                if count > h:
                    return False
            return True

        max_pile = max(piles)
        # sample_space = [i for i in range(1,max_pile+1)]

        left = 1
        right = max_pile
        ans = max_pile
        while left <= right:
            mid = (left+right)//2
            check_mid = check(mid)
            if check_mid:
                ans = mid
                right = mid-1
            else:
                left = mid+1

        return ans



        