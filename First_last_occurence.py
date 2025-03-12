# Given a sorted array arr with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.
# Note: If the number x is not found in the array then return both the indices as -1.

# Examples:

# Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
# Output: [2, 5]
# Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5


#  Brute Force O(N) complexity
def find(self, arr, x):
    first_pos=-1
    last_pos=0
    for i in range(len(arr)):
        if arr[i]==x:
            if first_pos==-1:
                first_pos=i
        if arr[i]==x and first_pos!=-1:
            last_pos=i
    if (first_pos==-1) and (last_pos==0):
        return (-1,-1)
    else:
        return (first_pos,last_pos)



# Efficient Approach O(logN) complexity - BST
def find_first_and_last(arr, x):
    def binary_search(left_search):
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == x:
                result = mid
                if left_search:
                    right = mid - 1  # Search on the left side
                else:
                    left = mid + 1   # Search on the right side
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    first = binary_search(left_search=True)
    last = binary_search(left_search=False)
    
    return [first, last]

# Example Usage
arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
x = 2
print(find_first_and_last(arr, x))  # Output: [1, 3]

x = 5
print(find_first_and_last(arr, x))  # Output: [6, 8]

x = 10
print(find_first_and_last(arr, x))  # Output: [-1, -1]
