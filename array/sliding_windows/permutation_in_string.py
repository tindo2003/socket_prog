from collections import defaultdict, Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N = len(s1)
        M = len(s2)
        if M < N: return False 
        s1_counter = Counter(s1)
        my_counter = defaultdict(int)
        def check_permutation(dict1, dict2):
            for key, val in dict1.items():
                if dict2[key] != val:
                    return False 
            return True
        for i in range(N):
            my_counter[s2[i]] += 1
        if check_permutation(s1_counter, my_counter): return True
        for i in range(N, M):
            cur_ele = s2[i]
            about_to_remove = s2[i-N]
            my_counter[about_to_remove] -= 1
            if my_counter[about_to_remove] == 0:
                del my_counter[about_to_remove]
            my_counter[cur_ele] += 1
            if check_permutation(s1_counter, my_counter): return True 

        return False

        
    
           