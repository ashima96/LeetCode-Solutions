class Solution:
    def twoSum(self, numbers, target):
        beg = 0
        end = len(numbers) - 1

        while beg < end:
            sm = numbers[beg] + numbers[end]
            if sm == target:
                return [beg + 1, end + 1]
            elif sm > target:
                end -= 1
            else:
                beg += 1


numbers = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(numbers, target))
