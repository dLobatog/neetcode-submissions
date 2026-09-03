class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        remaining = Counter(t)

        def is_valid():
            return all(value <= 0 for value in remaining.values())

        left = 0
        best_start = 0
        best_length = float("inf")

        for right, char in enumerate(s):
            # Add the right character.
            if char in remaining:
                remaining[char] -= 1

            # Shrink while the window remains valid.
            while is_valid():
                window_length = right - left + 1

                if window_length < best_length:
                    best_start = left
                    best_length = window_length

                # Remove the left character.
                left_char = s[left]
                if left_char in remaining:
                    remaining[left_char] += 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]