class Solution:
    """
    如果两个矩形相交，那么两者左边横坐标的最大值一定大于两者右边横坐标的最小值，
    两者下边纵坐标的最大值一定小于两者上边纵坐标的最小值。
    """
    def isRectangleOverlap(self, rec1 , rec2) -> bool:
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

        # return (rec1[2] > rec2[0] and  # left
        #             rec1[3] > rec2[1] and  # bottom
        #             rec1[0] < rec2[2] and  # right
        #             rec1[1] < rec2[3])    # top y1 y2