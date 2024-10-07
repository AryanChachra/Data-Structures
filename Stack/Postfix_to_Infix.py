def postfix_to_infix(s):
    stack=[]
    operators=set(['+','-','/','*','^'])
    
    for char in s:
        if char not in operators:
            stack.append(char)
        else:
            right_operand=stack.pop()
            left_operand=stack.pop()
        
            exp= f"({left_operand}{char}{right_operand})"
            stack.append(exp)
    return stack.pop()

def main():
    s=input()
    print(postfix_to_infix(s))

if __name__=="__main__":
    main()
