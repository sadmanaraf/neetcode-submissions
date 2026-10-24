class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        return " ".join([item[::-1] for item in arr])
       
