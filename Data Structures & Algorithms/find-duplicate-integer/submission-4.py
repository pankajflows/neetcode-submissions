class Solution:
    def findDuplicate2(self, nums: List[int]) -> int:
        # modifies the array
        for n in nums:
            if nums[abs(n)-1] < 0:
                return abs(n)
            nums[abs(n)-1] *= -1

    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow pointers
        tort = nums[nums[0]]
        hare = nums[nums[nums[0]]]

        while tort != hare:
            tort = nums[tort]
            hare = nums[nums[hare]]

        tort = nums[0]
        while tort != hare:
            tort = nums[tort]
            hare = nums[hare]

        return hare
        