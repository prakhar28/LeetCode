class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        while p < len(flowerbed) - 1:
            if flowerbed[p] == 1:
                p +=1
                continue
            if(flowerbed[p-1] == 0 and flowerbed[p+1] == 0):
                n -= 1
                if n == 0:
                    return "true"
            return "false"
        return "false"
