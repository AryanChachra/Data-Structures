def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    
def main():
    arr=[]
    n=int(input('Enter the size of the array: '))
    for i in range(n):
        val=int(input())
        arr.append(val)
    
    print(arr)
    insertion_sort(arr)
    print(arr)

if __name__=="__main__":
    main()
