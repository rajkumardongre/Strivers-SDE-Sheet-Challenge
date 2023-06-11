def isValidParenthesis(expression):
    stk = []
    for char in expression:
        if(char == '[' or char == '(' or char == '{'):
            stk.append(char)
        else:
            top = ''
            if(len(stk) > 0):
                top = stk.pop()
            else:
                return False
            if((char == '}' and top == '{') or (char == ']' and top == '[') or (char == ')' and top == '(')):
                continue
            else:
                return False        
    if len(stk) != 0:
        return False
    return True





# Main Code

t = int(input().strip())

for i in range(t):
    str = input().strip()
    ans = isValidParenthesis(str)

    if ans:
        print("Balanced")
        
    else:
        print("Not Balanced")
