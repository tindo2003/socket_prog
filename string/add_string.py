

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        add_on = 0 
        n1 = len(num1)
        n2 = len(num2)
        if n1 < n2:
            num1 = "0" * (n2 - n1) + num1
        else: 
            num2 = "0" * (n1 - n2) + num2 
        print(num1, num2)
        n = max(n1, n2)
        for idx in range(n - 1, -1, -1):
            print("add_on", add_on)
            digit1 = int(num1[idx])
            digit2 = int(num2[idx])
            tmp = digit1 + digit2 + add_on
            add_on = tmp // 10
            if add_on and idx != 0:
               res.append(str(tmp % 10))  
            else:
                res.append(str(tmp)) 
        print(res)           
        res.reverse()
        return "".join(res)

def main():
    sol = Solution()
    num1 = "11"
    num2 = "123"
    res = sol.addStrings(num1, num2)
    print(res)

if __name__ == "__main__":
    main()