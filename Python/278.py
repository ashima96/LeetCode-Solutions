# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
bad = 4
def isBadVersion(version):
    if version == bad:
        return True
    return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        beg = 1
        end = n
        found = []
        while beg <= end:
            mid = (end + beg)//2
            check = isBadVersion(mid)
            if check:
                end = mid-1
                found.append(mid)
            else:
                beg = mid+1
        return min(found)

n = 5
solution = Solution()        
print(solution.firstBadVersion(n))