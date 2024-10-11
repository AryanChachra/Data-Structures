def precedence(c):
    if c=='^':
        return 3
    elif c=='/' or c=='*':
        return 2
    elif c=='+' or c=='-':
        return 1
    else:
        return -1

def infix_to_postfix(s):
    result=[]
    stack=[]
    
    for c in s:
        if ('a'<= c <='z') or ('A'<= c <='Z') or ('0'<=c<='9'):
            result.append(c)
        elif c=='(':
            stack.append(c)
        elif c==')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and 
                   (precedence(c) < precedence(stack[-1]) or 
                    (precedence(c) == precedence(stack[-1]) and c != '^'))):
                result.append(stack.pop())
            stack.append(c)
        
    while stack :
        result.append(stack.pop())
    
    print(''.join(result))


def main():
    s=input()
    infix_to_postfix(s)
    
if __name__=='__main__':
    main()
