class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(ord('a')-97)
        # print(ord('z')-97)
        sets = {}
        for s in strs:
            alphabet_key = [0] * 26
            for char in s:
                alphabet_key[ord(char) - 97] += 1 

            alphabet_key = tuple(alphabet_key)
            if alphabet_key in sets:
                sets[alphabet_key].append(s)
            else:
                sets[alphabet_key] = [s]

        return list(sets.values())