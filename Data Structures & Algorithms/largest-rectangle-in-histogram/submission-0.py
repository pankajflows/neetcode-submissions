class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        incstack = [0]*len(heights)
        decstack = [0]*len(heights)

        stac = deque()
        for i in range(len(heights)-1, -1, -1):
            while stac and heights[stac[-1]] >= heights[i]:
                stac.pop()

            incstack[i] = stac[-1] if stac else len(heights)
            stac.append(i)

        stac = deque()
        for i in range(0, len(heights)):
            while stac and heights[stac[-1]] >= heights[i]:
                stac.pop()

            decstack[i] = stac[-1] if stac else -1
            stac.append(i)

        # print(incstack)
        # print(decstack)

        ans = 0
        for i in range(len(heights)):
            loc_area = heights[i] * (incstack[i] - decstack[i] - 1)
            ans = max(ans, loc_area)
            print(loc_area)

        return ans


        