class Solution:
    def climbStairs(self, n: int) -> int:
            memo = {}

            def helper(n):
                if n in memo:
                    return memo[n]

                if n == 0:
                    return 1
                if n == 1:
                    return 1

                result = helper(n-1) + helper(n-2)

                memo[n] = result

                return result
            
            return helper(n)