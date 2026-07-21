class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysArr = [0] * len(temperatures)

        currStack = [0]

        for i in range(1, len(temperatures)):
            while currStack:
                if temperatures[i] > temperatures[currStack[-1]]:
                    popped_index = currStack.pop()
                    daysArr[popped_index] = i - popped_index

                else:
                    currStack.append(i)
                            
        return daysArr