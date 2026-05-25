class Solution:
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        left1 = left2 = 0
        right1 = len(nums1)-1
        right2 = len(nums2)-1
        merged_left_length = math.ceil(len(nums1)+len(nums2)/2)

        while left1 <= right1 and left2 <= right2:
            mid1 = (left1+right1)//2
            mid2 = (left2+right2)//2

            if nums1[mid1] > nums2[mid2+1]:
                left1 = mid1

            if nums2[mid2] > nums1[mid1+1]:
                right1 = mid2

        return max(nums1[left1], nums2[left2])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        merged_left_length = (len(nums1)+len(nums2)+1) // 2
        left = 0
        right = len(nums1)
        
        while left <= right:
            mid = (left+right)//2
            mid1 = mid
            mid2 = merged_left_length - mid
            
            left1 = nums1[mid1-1] if mid1-1 >= 0 else -float("inf")
            right1 = nums1[mid1] if mid1 < len(nums1) else float("inf")

            left2 = nums2[mid2-1] if mid2-1 >= 0 else -float("inf")
            right2 = nums2[mid2] if mid2 < len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)

            if left1 > right2:
                right = mid-1
            elif left2 > right1:
                left = mid+1


        return 0.0



        