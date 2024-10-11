def prefix_to_postfix(s):
    stack=[]
    operators=set(['+','-','/','*','^'])
    for c in reversed(s):
        if c not in operators:
            stack.append(c)
        
        else:
            op1=stack.pop()
            op2=stack.pop()
            
            exp=f"{op1}{op2}{c}"
            stack.append(exp)
    
    return stack.pop()
        
def main():
    s=input()
    print(prefix_to_postfix(s))
    

if __name__=="__main__":
    main()
