# There is an integer array nums sorted in ascending order (with distinct values)
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4



#First approach is O(N) with two pointers

def search(self, nums, target: int) -> int:
    left=0
    right=len(nums)-1
    while left<=right:
        if nums[left]==target:
            return left
        elif nums[right]==target:
            return right
        else:
            left+=1
            right-=1
    return -1

# Second is binary search
def search_rotated(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check which half is sorted
        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # target is in the sorted left half
            else:
                left = mid + 1   # target is in the right half
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # target is in the sorted right half
            else:
                right = mid - 1  # target is in the left half