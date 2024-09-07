from typing import List 
class ATM:
    def __init__(self):
      self.amnts = [20, 50, 100, 200, 500]
      self.arr = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, freq in enumerate(banknotesCount):
          self.arr[idx] += freq
        

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * 5
        for idx in range(len(self.arr) - 1, -1, -1):
          # good idea
          bank_note_num = min(self.arr[idx], amount // self.amnts[idx])
          amount -= bank_note_num * self.amnts[idx]    
          ans[idx] = bank_note_num
        if amount > 0:
          return [-1]
        else:
          for idx, val in enumerate(ans):
            self.arr[idx] -= val
          return ans




# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)