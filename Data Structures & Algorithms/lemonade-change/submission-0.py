class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # pay with 5, 10, 20
        # each customer buys 1 lemonade and pays
        # always aim to keep the lowest denomination for the longest time?/
        #       5. 10  20
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                ten += 1 

            change = bill - 5

            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
            elif change == 15:
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                

        return True
            


                    
        