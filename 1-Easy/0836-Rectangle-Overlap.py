class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        x11, x12, x21, x22 = rec1[0], rec1[2], rec2[0], rec2[2]
        y11, y12, y21, y22 = rec1[1], rec1[3], rec2[1], rec2[3]

        res = (
            (min(x12,x22) > max(x11,x21))
            and (min(y12,y22) > max(y11,y21))
        )

        return res