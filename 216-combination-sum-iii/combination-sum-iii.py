class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res , curr_com = [] , []

        def backtrack(start , curr_som):
            if len(curr_com) == k and target == curr_som  :
                res.append(curr_com[:])
                return
            if len(curr_com) > k or curr_som > target:
                return
            
            for num in range(start,10):
                curr_com.append(num)
                backtrack(num+1 , curr_som + num)
                curr_com.pop()
        backtrack(1 , 0)
        return res