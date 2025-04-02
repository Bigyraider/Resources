def isPalindrome(self, s: str) -> bool:
    return s == s[::-1]

# Time complexity of above code is O(n) and space complexity of O(n)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    
    # Time complexity is same but space complexity is O(1)