class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        1. First check if len of s1 > than s2 this means that s2 can not have a perm of s1

        2. create our initial windows for s1 and s2 (freq map)

        3. check if our initial windows ==

        4. for r in range(len(s1), len(s2)):
                add r in window count
                -1 for l 

                check if s2[l] == 0 this means we need to remove the char from our freq map

                l += 1

                check if s1window == window count
                    return true else false
        '''

        s1count = {}
        window_count = {}

        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            s1count[s1[i]] = s1count.get(s1[i],0) + 1
            window_count[s2[i]] = window_count.get(s2[i],0) + 1

        if s1count == window_count:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
            window_count[s2[r]] = window_count.get(s2[r],0) + 1
            window_count[s2[l]] -= 1

            if window_count[s2[l]] == 0:
                del window_count[s2[l]]

            l += 1

            if window_count == s1count:
                return True
            
        return False