class Solution:
    '''
    create an empty dictionary, we are using defaultdict here so we don't have to handle empty

    for every word in our input we are first sorting it and then joining it ''.join(sorted(word))

    then use that sorted(word) as key as all anagrams will result to the same key 
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
        
            groups[key].append(word)
        
        return list(groups.values())