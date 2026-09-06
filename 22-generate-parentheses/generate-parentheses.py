class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(s, open, close):
            # Base case
            if len(s) == 2 * n:
                res.append(s)
                return

            # Add '('
            if open < n:
                backtrack(s + "(", open + 1, close)

            # Add ')'
            if close < open:
                backtrack(s + ")", open, close + 1)

        backtrack("", 0, 0)
        return res