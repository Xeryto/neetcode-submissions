class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-/*"

        for token in tokens:
            if token in operators:
                num2 = stack.pop(-1)
                num1 = stack.pop(-1)
                match token:
                    case "+":
                        stack.append(num1+num2)
                    case "-":
                        stack.append(num1-num2)
                    case "/":
                        result = num1/num2
                        if result < 0:
                            stack.append(math.ceil(result))
                        else:
                            stack.append(math.floor(result))
                    case "*":
                        stack.append(num1*num2)
            else:
                stack.append(int(token))
            
        return stack[-1]