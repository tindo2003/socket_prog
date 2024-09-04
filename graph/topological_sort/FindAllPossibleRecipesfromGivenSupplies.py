from typing import List 
from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies)
        recipe_set = set(recipes)
        adj_lst = defaultdict(list)
        for recipe, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                if ing in supplies_set or ing in recipe_set:
                    adj_lst.append(recipe)
        visited = set()
        def dfs(cur_node, path):
            for neighbor in cur_node:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
            path.appendleft(cur_node)
        for node in adj_lst.keys():
            if node not in visited:
                visited.add(node)
                path = deque([])
                dfs(node, path)
                print(path)


        