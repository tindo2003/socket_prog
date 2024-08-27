from typing import (
    List,
)
from collections import defaultdict
from itertools import combinations

class Solution:
    """
    @param username: An array with username
    @param timestamp: Timestamp of the user's visit to the website
    @param website: Websites visited by users
    @return: Most frequent access behavior
    """
    def most_visited_pattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # write your code here  
        G = defaultdict(list)
        for _, user, web in sorted(zip(timestamp, username, website)):
            G[user].append(web)
        
        scores = defaultdict(int)
        for user, web in G.items():
            for websites in combinations(web, 3):
                scores[websites] += 1
        
        max_pattern, max_val = "", 0 
        for k, v in scores.items():
            if v > max_val or (max_pattern > k and v == max_val):
                max_pattern = k 
                max_val = v 
        return max_pattern

def main():
    sol = Solution()
    username = ["usera","usera","usera","userb","userb","userb"]
    timestamp = [1,2,3,4,5,6]
    website = ["a","b","c","a","b","a"]
    res = sol.most_visited_pattern(username, timestamp, website)
    print(res)

if __name__ == "__main__":
    main()