class Solution:
    def trap2(self, height: List[int]) -> int:

        i = 0
        j = 1
        ans = 0

        while i < j and j < len(height):
            if height[i] <= height[j]:
                area = height[i] * (j-i-1)
                print(i, j, height[i], height[j], area)
                for m in range(i+1, j):
                    area -= height[m]
                    print("minus", m, height[m])
                ans += area
                i = j
            j += 1
        print("\n")
        j = i+1
        while i < j and j < len(height):
            if height[i] >= height[j]:
                area = height[i] * (j-i-1)
                print(i, j, height[i], height[j], area)
                for m in range(i+1, j):
                    area -= height[m]
                    print("minus", m, height[m])
                ans += area
                i = j
            # else:
            #     i += 1
            j += 1

        return ans
        
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)

        m = 0
        for i in range(len(height)):
            m = max(m, height[i])
            prefix[i] = m

        m = 0
        for i in range(len(height)-1, -1, -1):
            m = max(m, height[i])
            suffix[i] = m

        # print(prefix)
        # print(suffix)

        ans = 0
        for i in range(len(height)):
            ans += min(prefix[i], suffix[i]) - height[i]

        return ans


