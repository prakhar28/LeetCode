class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = {}
        invalidIndex = set()

        for i in range(len(transactions)):
            tempArr = transactions[i].split(",")
            tempArr.append(i)
            dic.setdefault(tempArr[0], []).append(tempArr)
        
        for key, value in dic.items():
            for v1 in value:
                if int(v1[2]) > 1000:
                    invalidIndex.add(v1[4])
                for v2 in value:
                    if v1 == v2:
                        continue
                    if abs(int(v1[1]) - int(v2[1])) <= 60 and v1[3] != v2[3]:
                        invalidIndex.add(v1[4])
        
        return [transactions[i] for i in invalidIndex ]



        
        