class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0

        currSum = 0
        for i in gain:
            currSum += i
            if currSum > maxAlt:
                maxAlt = currSum
        
        return maxAlt

