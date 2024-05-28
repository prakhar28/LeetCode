class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []

        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        
        pairs.sort(key=lambda x: x[0], reverse=True)

        for p, s in pairs:
            time = (target - p)/s
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)