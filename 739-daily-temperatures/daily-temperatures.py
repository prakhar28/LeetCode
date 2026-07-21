class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        daysArr = [0] * len(temperatures)

        currStack = [0]

        for i in range(len(temperatures)):
            while currStack and temperatures[i] > temperatures[currStack[-1]]:
                print("curSta, i", currStack, i)
                popped_index = currStack.pop()
                print("popi", popped_index)
                daysArr[popped_index] = i - popped_index
            currStack.append(i)

        return daysArr