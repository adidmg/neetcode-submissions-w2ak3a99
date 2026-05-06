class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper={'+','-','*','/'}
        for i in tokens:
            if i in oper:
                b=stack.pop()
                a=stack.pop()
                
                match i:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack[0]
