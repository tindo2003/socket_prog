class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    directions = [
      (0, 1),
      (-1, 0),
      (0, -1),
      (1, 0)
    ]
    pos = (0, 0)
    idx = 0

    for _ in range(4):
      for insn in instructions:
        if insn == "G":
          dx, dy = directions[idx]
          x, y = pos 
          nx, ny = dx + x, dy + y
          pos = (nx, ny)
        elif insn == "L":
          idx = (idx + 1 + 4) % 4 
        else:
          idx = (idx - 1 + 4) % 4 
    
    return pos == (0, 0)


def main():
  sol = Solution()
  instructions = "GL"
  res = sol.isRobotBounded(instructions)
  print(res)

if __name__ == "__main__":
  main()