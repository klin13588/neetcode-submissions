class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        iterate through all word in strs group them by keys

        anagrams will all result to the same keys 
        
        '''
        res = defaultdict(list)

        for word in strs:
            print(word)
            key = ''.join(sorted(word))
            res[key].append(word)
        
        return list(res.values())

        
