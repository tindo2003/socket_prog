class Solution:
  def brokenCalc(self, startValue: int, target: int) -> int:
    ans = 0
    while target > startValue:
        if target % 2 != 0:
            target += 1
        else:
            target /= 2
        ans += 1
    if target == startValue:
        return ans
    ans += (startValue - target)
    return int(ans)

def main():
  sol = Solution()
  start = 2
  target = 3
  res = sol.brokenCalck(start, target)
  print(res)

if __name__ == "__main__":
  main()