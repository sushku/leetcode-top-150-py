from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        With O(n) time and O(1) memory
        """
        if len(nums) <= 1:
            return 0
        jumps = 1
        left, right = 0, nums[0]
        while right < len(nums) - 1:
            jumps += 1
            next = max([j + nums[j] for j in range(left, right+1)])
            left, right = right, next
        return jumps

    def jump1(self, nums: List[int]) -> int:
        """
        WIth O(n) memory
        """
        minJumps = [0] * len(nums)
        found = False
        for i in range(len(nums)):
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                minJumps[j] = minJumps[i] + 1 if not minJumps[j] else minJumps[j]
                if j == len(nums) - 1:
                    found = True
                    break
            if found:
                break
        return minJumps[-1]

nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
#nums = [2,3,1,1,4]
#nums = [0]
s = Solution()
print(s.jump(nums))