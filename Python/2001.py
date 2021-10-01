class Solution:
    def finalValueAfterOperations(self, operations) -> int:
        result = 0
        for oper in operations:
            if "--" in oper:
                result -=1 
            else:
                result +=1
        return result

    
operations = ["--X","X++","X++"]
solution = Solution()
print(solution.finalValueAfterOperations(operations))