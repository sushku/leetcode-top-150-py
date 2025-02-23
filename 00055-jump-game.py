from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJumpFlg = True
        for i in range(len(nums) - 2, -1, -1):
            if canJumpFlg and nums[i] == 0:
                canJumpFlg = False
                zeroIndex = i
            if not canJumpFlg and nums[i] > zeroIndex - i:
                canJumpFlg = True
        return canJumpFlg

nums = [0, 1]
s = Solution()
print(s.canJump(nums))