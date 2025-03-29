# Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

# Note: If multiple occurrences are there, please return the smallest index.

#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        left = 0
        right = len(arr)-1
        index=-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid]==k:
                index=mid
                right=mid-1
            if arr[mid]<k:
                left=mid+1
            else:
                right=mid-1
        
        return (index)   
