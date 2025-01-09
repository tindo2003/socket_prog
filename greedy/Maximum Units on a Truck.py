from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        res = 0
        idx = 0
        while truckSize > 0 and idx < len(boxTypes):
            cur_num, cur_unit = boxTypes[idx]
            amnt_to_take = min(truckSize, cur_num)
            truckSize -= amnt_to_take
            res += amnt_to_take * cur_unit
            idx += 1
        return res
