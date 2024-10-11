def prefix_to_infix(s):
    stack=[]
    operators=set(['+','-','/','*','^'])
    
    for c in reversed(s):
        if c not in operators:
            stack.append(c)
        else:
            left_operand=stack.pop()
            right_operand=stack.pop()
            
            exp=f"({left_operand}{c}{right_operand})"
            stack.append(exp)
    
    return stack.pop()

def main():
    s=input()
    print(prefix_to_infix(s))

if __name__=='__main__':
    main()
