class Solution:
    def mySqrt(self, x: int) -> int:
    

        high = x
        low = 0


        while low <= high:
            mid = (high + low) // 2

            res = mid * mid
            
            if res == x:
                return mid
            elif res < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high
            

        