class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 1 xor 3 xor 5
        # 2 xor 5 = 7
        pref_sum = [arr[0]]
        cur = arr[0]
        for num in arr[1:]:
            cur ^= num 
            pref_sum.append(cur)
        res = []
        
        for query in queries:
            l, r = query[0], query[1]
            
            actual_l = l - 1
            if actual_l < 0:
                res.append(pref_sum[r])
            else:
                tmp = pref_sum[r] ^ pref_sum[l-1]
                res.append(tmp)
        return res
        