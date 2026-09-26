class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Convert the knowledge list into a hash map for O(1) lookups
        d = {key: val for key, val in knowledge}
        
        res = []
        is_inside_bracket = False
        current_key = []
        
        # Step 2: Iterate through the string character by character
        for char in s:
            if char == '(':
                is_inside_bracket = True
            elif char == ')':
                is_inside_bracket = False
                key_str = "".join(current_key)
                # O(1) lookup: append value if key exists, otherwise append "?"
                res.append(d.get(key_str, "?"))
                current_key = []  # Reset for the next bracket pair
            else:
                if is_inside_bracket:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)
