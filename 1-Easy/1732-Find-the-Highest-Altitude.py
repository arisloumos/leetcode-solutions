class Solution(object):
    def largestAltitude(self, gain):
        max_alt = 0
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            if alt > max_alt:
                max_alt = alt
        return max_alt
