class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        while p < len(flowerbed) - 1:            
            if(flowerbed[p-1] == 1 or flowerbed[p+1] == 1 or flowerbed[p] == 1):
                p+=1
                continue
            flowerbed[p] = 1
            n -= 1
            return True
        return False
