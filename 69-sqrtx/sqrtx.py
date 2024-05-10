class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l,r = 1,x
        ans = -1
        while l<=r:
            m = (l+r)//2
            mSq= m * m
            if mSq == x:
                return m
            elif mSq > x:
                r = m - 1 
            else:
                l = m + 1
                ans = m
        return ans