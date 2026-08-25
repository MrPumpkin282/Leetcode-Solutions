class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        x = 0
        for i in range(0,len(operations)):
            if operations[i] == 'D':
                x = int(record[-1]) * 2
                record.append(x)
            elif operations[i] == 'C':
                for i in range(0,len(record)):
                    record.remove(record[-1])
                    break
            elif operations[i] == '+':
                for i in range(0,len(record)):
                    record.append(int(record[-1]) + int(record[-2]))
                    break
            else:
                record.append(int(operations[i]))
        return sum(record)
                    





        