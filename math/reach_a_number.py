class Solution:
  def reachNumber(self, target: int) -> int:
    steps = 0
    cur_sum = 0
    cur_num = 1

    while True:
      cur_sum += cur_num
      steps += 1
      sum_parity = cur_sum % 2 
      target_parity = target % 2
      if cur_sum >= target and sum_parity == target_parity:
        return steps
      cur_num += 1

def main():
  sol = Solution()
  target = 12
  res = sol.reachNumber(target)  
  print(res)

if __name__ == "__main__":
  main()