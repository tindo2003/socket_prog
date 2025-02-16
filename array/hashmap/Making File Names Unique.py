from typing import List
from collections import defaultdict


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # Dictionary tracking the next smallest version number for each file name
        my_dict = defaultdict(int)
        res = []

        for name in names:
            if name not in my_dict:
                res.append(name)
                my_dict[name] = 0
            else:
                # If the name already exists, find an available version by incrementing
                next_id = my_dict[name] + 1
                candidate_str = f"{name}({next_id})"

                # Continue incrementing until a unique name is found
                while candidate_str in my_dict:
                    next_id += 1
                    candidate_str = f"{name}({next_id})"

                res.append(candidate_str)

                # the smallest you can do. this takes care of the case when you have "hi", "hi(1)", "hi(2)". the next time you put "hi", your next id will becomes 3
                my_dict[name] = next_id
                # keep track of candidate_str just in case. if file "hi(3)" is inputed in the future, it should become hi(3)(1) cuz hi(3) is already inputted above.
                my_dict[candidate_str] = 0

        return res
