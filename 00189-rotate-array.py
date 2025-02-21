from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Using O(1) space
        """
        k %= len(nums)
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        print(nums)

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Using O(n) space
        """
        k = k % len(nums)
        if k > 0:
            mem = nums[-k:]
            rem = len(nums) - k
            nums[-rem:] = nums[:rem]
            nums[:k] = mem

nums, k = [1, 2, 3, 4, 5, 6, 7], 9
s = Solution()
s.rotate(nums, k)