class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # limit = max weight
        # how to combine this most efficiently? pick heaviest possible then small?
        people.sort()
        l, r = 0, len(people)-1
        count = 0

        while l <= r:
            if l < r and people[l] + people[r] <= limit:
                l += 1  # Lightest joins the heaviest.

            r -= 1      # Heaviest always takes this boat.
            count += 1

        return count
