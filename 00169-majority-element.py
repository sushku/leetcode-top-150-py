from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Moore's voting algorithm
        """
        i, count = 0, 0
        major = None
        while i < len(nums):
            if major == None:
                major = nums[i]
                count += 1
                i += 1
                continue
            if nums[i] != major:
                if count == 0:
                    major = nums[i]
                    count += 1
                else:
                    count -= 1
            else:
                count += 1
            i += 1
        return major

    def majorityElement1(self, nums: List[int]) -> int:
        """
        Hash map method
        """
        i = 0
        d = {}
        while i < len(nums):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            i += 1
        for val, count in d.items():
            if count >= len(nums) / 2:
                return val

nums = [2,2,1,1,2,2,3,2,2,0,0,4,2,6,2,3,2]
s = Solution()
s.majorityElement(nums)