class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_pare , close_pare , curr):
            if len(curr) == 2*n :
                res.append("".join(curr))
                return

            if open_pare < n : 
                curr.append("(")
                backtrack(open_pare+1 , close_pare , curr)
                curr.pop()
            if open_pare > close_pare :
                curr.append(")")
                backtrack(open_pare , close_pare+1 , curr)
                curr.pop()

        backtrack(0,0,[])
        return res

