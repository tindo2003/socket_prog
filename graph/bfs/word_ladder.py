from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.extend([beginWord, endWord])
        wordList = list(set(wordList))

        def is_adjacent(s1, s2) -> bool:
            cnt = 0
            for a, b in zip(s1, s2):
                if a != b:
                    cnt += 1
            return cnt <= 1

        adj_lst = defaultdict(list)
        N = len(wordList)
        for i in range(N):
            cur_ele = wordList[i]
            for j in range(i + 1, N):
                neighbor_ele = wordList[j]
                if is_adjacent(cur_ele, neighbor_ele):
                    adj_lst[cur_ele].append(neighbor_ele)
                    adj_lst[neighbor_ele].append(cur_ele)

        q = [beginWord]
        best = defaultdict(int)
        best[beginWord] = 1
        while q:
            cur = q.pop(0)
            if cur == endWord:
                return best[cur]
            for neighbor in adj_lst[cur]:
                if neighbor not in best:
                    best[neighbor] = best[cur] + 1
                    q.append(neighbor)
        return 0
