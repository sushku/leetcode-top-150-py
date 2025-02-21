from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        More optimized solution
        """
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        print(k, nums)
        return k

    def removeDuplicates1(self, nums: List[int]) -> int:
        """
        Initially accepted solution
        """
        i, k = 0, 0
        prevNum = "Not set"
        while i < len(nums):
            if prevNum == "Not set":
                prevNum = nums[i]
                nums[k] = nums[i]
                count = 1
                i += 1
                k += 1
                continue
            if nums[i] == prevNum and count < 2:
                nums[k] = nums[i]
                count += 1
                i += 1
                k += 1
            elif nums[i] != prevNum:
                nums[k] = nums[i]
                prevNum = nums[i]
                count = 1
                i += 1
                k += 1
            else:
                i += 1
        return k

nums = [-1, 0, 0, 0, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 5, 5]
s = Solution()
s.removeDuplicates(nums)