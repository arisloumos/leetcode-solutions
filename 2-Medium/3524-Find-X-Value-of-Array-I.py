class Solution(object):
    def resultArray(self, nums, k):
        count0, count1, result = [0] * k, [0] * k, [0] * k

        for i in range(len(nums)):
            count1[nums[i] % k] += 1

            for j in range(k):
                if count0[j] > 0:
                    rem = j * nums[i] % k 
                    count1[rem] += count0[j]

            for x in range(k):
                result[x] += count1[x]

            count0[:], count1 = count1, [0] * k
            
        return result 