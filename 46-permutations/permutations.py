class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res , perma = [] , []

        def backtrack():
            if len(perma) == len(nums):
                res.append(perma[:]) 
                return
            

            for num in nums : 
                if num not in perma :
                    perma.append(num)
                    backtrack()
                    perma.pop()
            
        backtrack()
        return res