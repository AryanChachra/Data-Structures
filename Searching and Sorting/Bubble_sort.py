def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True

        if swapped == False:
            break

def main():
    arr=[]
    n=int(input('Enter the size of the array: '))
    for i in range(n):
        val=int(input())
        arr.append(val)
    
    print(arr)
    bubble_sort(arr)
    print(arr)

if __name__=="__main__":
    main()
