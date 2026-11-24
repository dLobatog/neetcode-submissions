class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # empty record initially
        # operations[i] is the ith opration to apply to record
        # either 'x', '+' (sum previous 2 scores), 'D, double previous', 'c' remove previous
        # when reading integer, add to record
        # when reading symbol, pop from record and apply
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == 'C':
                record.pop() 
            else:
                record.append(int(op))
            # print(record)

        return sum(record)