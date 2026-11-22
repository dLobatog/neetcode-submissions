class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(h)
        result = []
        while h:
            # pop from h
            freq, char = heapq.heappop(h)
            # print(result, freq, char)
            if len(result) >= 1 and result[-1] == char:
                # pop another option then, push the previous one
                if len(h) == 0:
                    return ""
                orig_freq, orig_char = freq, char
                freq, char = heapq.heappop(h)
                # push back the original
                heapq.heappush(h, (orig_freq, orig_char))
            # use it
            freq *= -1
            freq -= 1
            result.append(char)
            if freq != 0:
                heapq.heappush(h, (-freq, char))
            # if len(result) > len(s):
            #     return ''

        return ''.join(result)

