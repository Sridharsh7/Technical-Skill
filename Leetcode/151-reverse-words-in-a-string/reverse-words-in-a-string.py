class Solution:
    def reverseWords(self, s: str) -> str:
      c = s.split()
      reverse = c[::-1]
      a = ' '.join(reverse)
      return a +""
