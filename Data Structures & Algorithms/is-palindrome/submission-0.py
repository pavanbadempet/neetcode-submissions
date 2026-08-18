class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [x.lower() for x in s if x.isalnum()]
        return filtered == filtered[::-1]