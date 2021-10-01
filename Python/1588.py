class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        length = 1
        res = 0
        while length <= len(arr):
            for i in range(len(arr)):
                subarr = arr[i : i+length]
                if len(subarr) == length:
                    res += sum(subarr)
            length += 2
        return res   


arr = [1,4,2,5,3]
solution = Solution()
print(solution.sumOddLengthSubarrays(arr))