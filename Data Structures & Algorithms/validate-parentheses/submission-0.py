class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map closing brackets to their matching opening brackets
        matching = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in matching:
                # If stack has items and the top item matches the required opening bracket
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
            else:
                # It's an opening bracket, add to stack
                stack.append(char)
                
        # Valid only if all opened brackets were matched and popped
        return len(stack) == 0