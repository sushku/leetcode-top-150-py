from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, k = 0, 0
        while i < len(nums):
            if nums[i] != val:
                nums[k] = nums[i]
                i += 1
                k += 1
            else:
                i += 1
        return k

nums, val = [2, 2, 2, 8, 9, 7, 7, 7], 2
s = Solution()
s.removeElement(nums, val)
