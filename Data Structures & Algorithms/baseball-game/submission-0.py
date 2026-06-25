class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []


        for ops in operations:
            if ops.lstrip('-').isdigit():
                record.append(int(ops))
            elif ops == "+" and len(record) >= 2:
                record.append(record[-1] + record[-2])
            elif ops == "C":
                record.pop()
            elif ops == "D":
                record.append(record[-1] *  2)
                
        
        return sum(record)

        
        
        