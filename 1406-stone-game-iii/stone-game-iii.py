class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4

        for i in range(n-1, -1, -1):
            take = 0
            best = float('-inf')

            for k in range(1,4):
                if i + k <=n:
                    take += stoneValue[i+k-1]
                    best = max(best, take - dp[(i+k) % 4])
            dp[i % 4] = best
        diff = dp[0]


        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"