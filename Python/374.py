# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
pick = 6
def guess(num: int) -> int:
    if num < pick:
        return 1
    elif num > pick:
        return -1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        beg = 1
        end = n
        while beg <= end:
            mid = (beg+end)//2
            check = guess(mid)
            if check == 0:
                return mid
            elif check == -1:
                end = mid - 1
            else:
                beg = mid + 1


n = 10
solution = Solution()
print(solution.guessNumber(n))