from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i, h = 0, 0
        while i < len(citations):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
            i += 1
        return h

#citations = [3, 0, 6, 1, 5]
#citations = [9, 8, 5, 2, 1, 0]
#citations = [1, 1, 1, 1, 1]
citations = [1]
s = Solution()
print(s.hIndex(citations))