from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0: 
                stack.append(asteroid)
                continue 
            
            destroyed = False
            while stack:
                prev = stack[-1]
                if prev < 0: break  # no collision 

                if abs(prev) > abs(asteroid): # top beats cur
                    destroyed = True
                    break 
                
                if abs(prev) == abs(asteroid): # both explodes
                    stack.pop()
                    destroyed = True 
                    break

                if abs(prev) < abs(asteroid):
                    stack.pop()
                    continue 

            if not destroyed:
                stack.append(asteroid)

        return stack




def main():
    sol = Solution()
    asteroids = [10,2,-5]
    res = sol.asteroidCollision(asteroids)
    print(res)

if __name__ == "__main__":
    main()