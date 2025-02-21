from typing import List

class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            if i < 0 or (j >= 0 and nums2[j] >= nums1[i]):
                nums1[k] = nums2[j]
                j = j - 1
            else:
                nums1[k] = nums1[i]
                i = i - 1
            k = k - 1

nums1, m = [-3, -2, -1, 0, 0, 0, 0], 4
nums2, n = [1, 1, 1], 3
s = Solution()
s.merge(nums1, m, nums2, n)
