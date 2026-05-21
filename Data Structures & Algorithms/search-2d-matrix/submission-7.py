class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Recursive
        def binary_array(start, end):
            # print(start, end)
            if start == end:
                return start if matrix[start][0] <= target else -1

            if start + 1 == end:
                if matrix[end][0] <= target:
                    return end
                return start if matrix[start][0] <= target else -1

            mid = (start+end) // 2

            if matrix[start][0] <= target < matrix[mid][0]:
                return binary_array(start, mid-1)
            else:
                return binary_array(mid, end)

        def binary_search(start, end, nums):
            if start == end:
                return start if nums[start] == target else -1

            mid = (start+end) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binary_search(start, mid, nums)
            else:
                return binary_search(mid+1, end, nums)

        final_array = binary_array(0, len(matrix)-1)
        # print(final_array)
        final_index = binary_search(0, len(matrix[final_array])-1, matrix[final_array])
        # print(final_index)
        return True if final_index >= 0 else False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # iterative

        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = (left+right) // 2
            # print("lr mid", left, right, mid)
            if target < matrix[mid][0]:
                right = mid-1
            elif target >= matrix[mid][0]:
                left = mid+1

        final_array = matrix[right]
        # print(right)

        left = 0 
        right = len(final_array)-1
        index = -1
        while left <= right:
            mid = (left+right) // 2
            # print("lrm", left, right, mid)
            if target == final_array[mid]:
                index = mid
                break
            elif target < final_array[mid]:
                right = mid-1
            else:
                left = mid+1

        # print(index)
        return True if index >= 0 else False
        


