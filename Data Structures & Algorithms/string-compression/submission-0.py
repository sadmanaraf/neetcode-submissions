class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0                                   # next slot to write into
        start = 0                                   # where the current group began
        for i in range(1, len(chars) + 1):
            if i == len(chars) or chars[i] != chars[start]:   # the group chars[start:i] ended
                chars[write] = chars[start]
                write += 1
                length = i - start
                if length > 1:
                    for digit in str(length):       # 12 -> '1', '2'
                        chars[write] = digit
                        write += 1
                start = i
        return write