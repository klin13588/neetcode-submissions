class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       '''
       so basically we are using bucket sort where the indices is going to represent the count
       of a num and for the value of that index we place the number that has that count

       so first we are looping through our input to get an initial count 

       then create a bucket of empty list that is equal to the size of our input as the top frequent
       can be at most the size of our input

       grab the key-value pair and insert into the bucket freq[c].append(num)

       then you would loop through the bucket in reverse for i in range(len(freq) -1, 0, -1)
       
       append to the res and then check if the length of our res is == k -> return res
       
       '''
       count = {}
       freq = [[] for i in range(len(nums) + 1)]

       for num in nums:
        count[num] = count.get(num, 0) + 1
       for num, c in count.items():
        freq[c].append(num)
       res = []

       for i in range(len(freq) - 1, 0, -1):
         for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
       
       
     