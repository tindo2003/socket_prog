from typing import List
class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    events = []

    START = 0
    END = 1

    for idx, (start, end) in enumerate(points):
      events.append((start, START, idx))
      events.append((end, END, idx))

    events.sort()
    
    ans = 0 
    bursted = [False] * len(points)
    interseting = []

    for time, status, idx in events:
      if status == END:
        if not bursted[idx]:
          for i in interseting:
            bursted[i] = True
          interseting = []
          ans += 1
      else:
        interseting.append(idx)

    return ans
        
def main():
  sol = Solution()
  points = [[1,2],[3,4],[5,6],[7,8]]
  res = sol.findMinArrowShots(points)
  print(res)

if __name__ == "__main__":
  main()