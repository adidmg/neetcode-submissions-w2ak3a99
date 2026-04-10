class Solution:
    def isValid(self, s: str) -> bool:
        par_dict={'}':'{', ']':'[', ')':'('}
        par_values=par_dict.values()
        stack=[]
        valid=False
        for i in s:
            if i in par_values:
                stack.append(i)
            elif i in par_dict:
                if len(stack)==0 or stack[-1]!=par_dict[i]:
                   return False
                else:
                    stack.pop()     
        return True if not stack else False


        