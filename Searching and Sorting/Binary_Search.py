def binary_search(arr,low,high,x):
    while low<=high:
        mid = low+(high-low) // 2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1

def main():
    arr=[]
    n=int(input('Enter the size of the array: '))
    for i in range(n):
        val=input()
        arr.append(val)
    x=input('Enter the element to search: ')
    element = binary_search(arr,0,len(arr)-1,x)
    print('element found at: ', element)

if __name__=="__main__":
    main()
