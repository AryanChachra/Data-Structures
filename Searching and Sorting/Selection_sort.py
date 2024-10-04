def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        minl=i
        for j in range(i+1,n):
            if arr[j]<arr[minl]:
                minl=j
        
        if minl != i:
            arr[i], arr[minl] = arr[minl], arr[i]



def main():
    arr=[]
    n=int(input('Enter the size of the array: '))
    for i in range(n):
        val=int(input())
        arr.append(val)
    print(arr)
    selection_sort(arr)
    print(arr)

if __name__=="__main__":
    main()
