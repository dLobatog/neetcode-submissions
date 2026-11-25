import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # pick a pivot
        #   iterate and put nums < pivot, nums > pivot 
        #.  do it over and over until no numbers
        def qs(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[random.randint(0, len(arr)-1)]
            lt, gt, eq = [], [], []
            for n in arr:
                if n == pivot:
                    eq.append(n)
                elif n > pivot:
                    gt.append(n)
                else:
                    lt.append(n)

            # print(lt, eq, gt)
            return qs(lt) + eq + qs(gt)

        return qs(nums)