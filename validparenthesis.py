import unittest
def isValid(s: str) -> bool:
    '''
    -if brac not in dict, put it in the stack
    -if in dict(meaning its a closing brac), check if the top of the stack is the
    same as the value for that brac in the dict. if so pop the stack
    -else return false
    '''

    bracket_maps = {")":"(","}":"{","]":"["}
    stack = []
    if len(s) <= 1 :
        return False

    for brac in s:
        if brac not in bracket_maps:
            stack.append(brac)
            
        else:
            if stack:
                if bracket_maps[brac] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                return False
    return len(stack) == 0
        
    

class TestingValidParenthesis(unittest.TestCase):
    def edgecases(self):
        self.assertEqual(isValid(" "), False)
        self.assertEqual(isValid("a"), False)
    def testCases(self):
        self.assertEqual(isValid("(()"), False)
        self.assertEqual(isValid("((()))"), True)
        self.assertEqual(isValid("(("), False)
        self.assertEqual(isValid("))))"), False)

if __name__ == '__main__':
    unittest.main()

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''