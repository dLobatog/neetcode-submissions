class Solution:
    # Encoded list of strings, needs a unique char separator
    # If only 256 valid ASCII... then use a non-ASCII character to encode
    # e.g: non-ascii 一 (1 in chinese)

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        result = []
        for s in strs:
            result.append(s)
            result.append("一")
        # print(result)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        tmp = []
        for c in s:
            if c != '一':
                tmp.append(c)
            else:
                result.append(''.join(tmp))
                tmp = []
        if tmp != []:
            result.append(''.join(tmp))

        return result
