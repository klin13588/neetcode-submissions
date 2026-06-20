class Solution:
    def isValid(self, s: str) -> bool:

        '''
        [(])

        stack = [[,(]

        we store the opening parintheses in a stack and once we see a closing we pop off the stack

        ([{}])

        stack = ([{

        }{
        ][
        
        '''
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for parintheses in s:
            if parintheses in closeToOpen:
                if stack and stack[-1] == closeToOpen[parintheses]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parintheses)
        return True if not stack else False
            