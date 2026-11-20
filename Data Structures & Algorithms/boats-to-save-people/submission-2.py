class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # limit = max weight
        # how to combine this most efficiently? pick heaviest possible then small?
        count = [0] * (max(people)+1)
        for p in people:
            count[p] += 1
        
        arr = []
        for i, c in enumerate(count):
            if c != 0:
                arr += [i] * c

        l, r = 0, len(arr)-1
        count = 0

        while l <= r:
            if l < r and arr[l] + arr[r] <= limit:
                l += 1  # Lightest joins the heaviest.

            r -= 1      # Heaviest always takes this boat.
            count += 1

        return count
