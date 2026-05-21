class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_array(start, end):
            print(start, end)
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
        print(final_array)
        final_index = binary_search(0, len(matrix[final_array])-1, matrix[final_array])
        print(final_index)
        return True if final_index >= 0 else False