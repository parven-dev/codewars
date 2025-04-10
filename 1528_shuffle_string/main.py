class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        
        my_indices = [""] * len(s)
        
        for i in range(len(indices)):
            my_indices[indices[i]] = s[i]
        return "".join(my_indices)
            
    
    
    
    
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
s1 = Solution()
print(s1.restoreString(s, indices))