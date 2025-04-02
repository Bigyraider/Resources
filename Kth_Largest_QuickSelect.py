def kth_largest(arr, k):
    k=len(arr)-k
    def quickselect(l,r):
        pivot,p = arr[r],l
        for i in range(l,r):
            if arr[i]<=pivot:
                arr[p],arr[i]=arr[i],arr[p]
                p+=1
        arr[p],arr[r]=arr[r],arr[p]

        if p==k:
            return arr[p]
        elif p<k:
            return quickselect(p+1,r)
        else:
            return quickselect(l,p-1)
    return quickselect(0,len(arr)-1)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_largest(arr,k))