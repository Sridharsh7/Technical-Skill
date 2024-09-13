class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort = sorted(s)
        sort1 = sorted(t)
        return sort == sort1