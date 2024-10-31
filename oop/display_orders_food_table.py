from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        all_food = set()
        my_tables = defaultdict(lambda: defaultdict(int))
        for name, table_num, dish in orders:
            all_food.add(dish)
            dish_freq = my_tables[table_num]
            dish_freq[dish] += 1
        dish_names = list(all_food)
        dish_names.sort()
        first_list = ["Table"] + dish_names
        
        res = []
        for table_num, dish_dict in my_tables.items():
            my_lst = [table_num]
            for dish_name in dish_names:
                my_lst.append(str(dish_dict[dish_name]))
            res.append(my_lst)
        res.sort(key=lambda x: int(x[0]))
        bruh = [first_list] + res
        return bruh
