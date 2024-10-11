def postfix_to_prefix(s):
    stack=[]
    operators=set(['+','-','/','*','^'])
    
    for c in s:
        if c not in operators:
            stack.append(c)
        
        else:
            op2=stack.pop()
            op1=stack.pop()
            
            exp=f"{c}{op1}{op2}"
            stack.append(exp)
    
    return stack.pop()

def main():
    s=input()
    print(postfix_to_prefix(s))

if __name__=="__main__":
    main()
