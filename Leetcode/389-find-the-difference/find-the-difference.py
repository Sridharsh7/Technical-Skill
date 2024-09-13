class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = sum(ord(x) for x in t)
        ss = sum(ord(x) for x in s)
        
        return chr(st - ss)