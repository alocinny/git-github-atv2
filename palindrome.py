class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        empty = ""
        for ch in reversed(string):
            empty = empty + ch
        
        if x == empty:
            return True
        else :
            return False
    
