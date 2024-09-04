from typing import List 
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(int)
        for cpdomain in cpdomains:
            visit_cnt, subdomain = cpdomain.split(" ")
            domains = subdomain.split(".")
            for idx in range(len(domains)-1,-1,-1):
                tmp_str = ".".join(domains[idx:])
                counter[tmp_str] += int(visit_cnt)
        res = []
        for key, val in counter.items():
            res.append(f"{key} {val}")
        return res 
        
