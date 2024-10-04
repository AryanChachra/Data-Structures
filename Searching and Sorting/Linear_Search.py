def linear_search(arr, n, x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1

def main():
    arr=[]
    n=int(input('enter the size of array'))
    for i in range(n):
        val = input()
        arr.append(val)
    x=input('enter the element to search')

    element = linear_search(arr,n,x)
    print('element found at index: ', element)

if __name__=="__main__":
    main()
