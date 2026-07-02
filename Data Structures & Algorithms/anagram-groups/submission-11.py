class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        have a hashmap that contains the sorted word as key add to that key

        return the dict.items() or values()
        '''

        res = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            res[key].append(word)
        
        return list(res.values())