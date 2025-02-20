from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 0
        prevNum = "Not set"
        while i < len(nums):
            if prevNum == "Not set":
                prevNum = nums[i]
                i += 1
                k += 1
                continue
            if nums[i] != prevNum:
                prevNum = nums[i]
                nums[k] = nums[i]
                i += 1
                k += 1
            else:
                i += 1
        print(k, nums)
        return k

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
s.removeDuplicates(nums)