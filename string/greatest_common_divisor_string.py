class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        latest_idx = -1
        def find_gcd(a, b):
            if b == 0:
                return a
            return find_gcd(b, a % b)

        wanted_length = find_gcd(len(str1), len(str2))
        if str1[:wanted_length] != str2[:wanted_length]: return ""
        candidate = str1[:wanted_length]

        for idx in range(wanted_length, len(str1), wanted_length):
            if str1[idx: idx + wanted_length] != candidate:
                return ""
        
        for idx in range(wanted_length, len(str2), wanted_length):
            if str2[idx: idx + wanted_length] != candidate:
                return ""
        
        return candidate
        