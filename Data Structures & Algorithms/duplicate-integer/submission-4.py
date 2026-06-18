class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # x = something to store int values from the array
        x = set() 
        #keep looping if this value is in x then return true else add it to the map

        for i in nums:
            if i in x:
                return True
            else:
                x.add(i)
        return False


