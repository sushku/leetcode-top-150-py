class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

sentence = "  the sky is   blue  "
s = Solution()
print(s.reverseWords(sentence))