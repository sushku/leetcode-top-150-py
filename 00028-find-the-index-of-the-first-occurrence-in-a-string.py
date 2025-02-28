class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

haystack = "asdfgh"
needle = "fgh"
s = Solution()
print(s.strStr(haystack, needle))