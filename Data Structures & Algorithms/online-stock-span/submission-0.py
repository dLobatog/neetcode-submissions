class StockSpanner:

    def __init__(self):
        self.s = []
        

    def next(self, price: int) -> int:
        # print(self.s, price)
        if len(self.s) > 0:
            if self.s[-1] > price:
                self.s.append(price)
                return 1
            else:
                cnt = 1
                for i in range(len(self.s)-1, -1, -1):
                    if self.s[i] <= price:
                        cnt += 1
                    else:
                        break
                self.s.append(price)
                return cnt

        else:
            self.s.append(price)
            return 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)