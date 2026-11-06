class Solution:
    def romanToInt(self, s: str) -> int:
        vocab = {'I': 1,'V':5,'X' :10 ,'L' : 50,'C': 100,'D': 500,'M': 1000}
        output = 0
        i = 0
        while i < len(s):
            if i < len(s)-1:
                if s[i:i+2] == 'IV':
                    output += 4
                    i += 2
                    continue
                elif s[i:i+2] == 'IX' :
                    output += 9
                    i += 2
                    continue
                elif s[i:i+2] == 'XL' :
                    output += 40
                    i += 2
                    continue
                elif s[i:i+2] == 'XC' :
                    output += 90
                    i += 2
                    continue
                elif s[i:i+2] == 'CD' :
                    output += 400
                    i += 2
                    continue
                elif s[i:i+2] == 'CM' :
                    output += 900
                    i += 2
                    continue
            output += vocab[s[i]]
            i += 1
        return output