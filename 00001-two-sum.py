class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, val in enumerate(nums):
            rem = target - val
            if rem in d:
                return i, d[rem]
            else:
                d[val] = i

# Main
nums = [1, 2, 3, 1]
target = 6
print(Solution().twoSum(nums, target))