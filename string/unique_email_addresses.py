from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            splits = local_name.split(".")
            joined = "".join(splits)
            splits = joined.split("+")
            res.add(f"{splits[0]}@{domain_name}")
        return len(res)
