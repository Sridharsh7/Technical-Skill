class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        for i in s:
            return len(a[-1])