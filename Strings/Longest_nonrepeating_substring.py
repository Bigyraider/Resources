def lengthOfLongestSubstring(self, s: str) -> int:
    i, j = 0, 0
    ans = 0
    seen = set()
    
    while j < len(s):
        if s[j] not in seen:
            seen.add(s[j])
            ans = max(ans, j - i + 1)
            j += 1
        else:
            seen.remove(s[i])
            i += 1
            
    return ans