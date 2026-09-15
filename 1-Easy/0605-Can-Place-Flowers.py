class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        new_plants = 0

        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i-1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)
            ):
                new_plants += 1
                flowerbed[i] = 1
        
        return new_plants >= n