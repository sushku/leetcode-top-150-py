class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in range(len(t)):
            if i == len(s):
                break
            if t[j] == s[i]:
                i += 1
        return True if i == len(s) else False

sub = "ace"
full = "abcdef"
s = Solution()
print(s.isSubsequence(sub, full))