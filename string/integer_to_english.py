class Solution:
    def numberToWords(self, num: int) -> str:
      if num == 0:
        return "Zero"
      my_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
      def get_string(n):
        '''
        n is 3 digits
        '''
        res = []
        hundreds = n // 100
        if hundreds != 0:
          res.append(my_dict[hundreds] + " Hundred")
        last_2 = n % 100
        if last_2 >= 20:
          tens, ones = last_2 // 10, last_2 % 10
          res.append(my_dict[tens * 10])
          if ones != 0:
            res.append(my_dict[ones])
        elif last_2 != 0:
          res.append(my_dict[last_2])
        return " ".join(res)
      post_fix = ["", " Thousand", " Million", " Billion"]
      i = 0
      res = []
      while (num != 0):
        digits = num % 1000
        s = get_string(digits)
        if len(s) > 0:
          res.append(s + post_fix[i])
        num = num // 1000
        i += 1
      res.reverse()
      return " ".join(res)


def main():
   sol = Solution()
   res = sol.numberToWords()
   print(res)
if __name__ == "__main__":
  main()