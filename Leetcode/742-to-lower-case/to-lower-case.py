class Solution:
    def toLowerCase(self, s: str) -> str:
        result=""
        for i in s:
            if 'A'<= i <= 'Z':
                result= result + chr(ord(i)+32)
            else:
                result=result + i
        return result