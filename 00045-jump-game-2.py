from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                minJumps[j] = minJumps[i] + 1 if not minJumps[j] else minJumps[j]
        return minJumps[-1]

# nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
nums = [1,1,1,1]
s = Solution()
print(s.jump(nums))