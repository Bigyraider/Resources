# Given an array arr[] and an integer k where k is smaller than the size of the array, your task is to find the kth smallest element in the given array.

# Follow up: Don't solve it using the inbuilt sort function.

# Examples :

# Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7
# Explanation: 3rd smallest element in the given array is 7.

def kth_smallest(arr, k):
    def Quicksort(l,r):
        pivot,p=arr[r],l
        for i in range(l,r):
            if arr[i]<=pivot:   #check if element is less than or equal to pivot
                arr[p],arr[i]=arr[i],arr[p]    #Swap value itself.
                p+=1
        arr[p],arr[r]=arr[r],arr[p]   #swapping arr[r] with arr[p] where the value becomes bigger than pivot

        if k-1 == p:
            return arr[p]
        elif k-1 < p:
            return Quicksort(l,p-1)
        else:
            return Quicksort(p+1,r)
    return Quicksort(0,len(arr)-1)

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr,k))