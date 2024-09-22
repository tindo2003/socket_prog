class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        my_set = set(['a','e','i','o','u'])
        vowel_cnt = 0
        ans = 0
        for i in range(k):
            if s[i] in my_set: vowel_cnt += 1
        ans = vowel_cnt
        for idx in range(k, len(s)):
            c = s[idx]
            prev_ele = s[idx - k]
            if prev_ele in my_set: vowel_cnt -= 1
            if c in my_set: vowel_cnt += 1
            ans = max(ans, vowel_cnt)
            
        return ans
