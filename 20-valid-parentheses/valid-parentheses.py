class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to store matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack exists, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the brackets match
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
        
        # Stack should be empty if all brackets are closed properly
        return not stack