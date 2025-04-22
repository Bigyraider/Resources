# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# You need to solve this problem without utilizing the built-in sort function.

def sort012(self, arr):
    mid = 0
    low = 0
    high = len(arr)-1
    
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr