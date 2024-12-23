class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            destroyed = False
            # moving left
            if a < 0:
                val_a = abs(a)
                while stack:
                    top = stack[-1]
                    # if this one is also moving left, nothing to destroy, quit
                    if top < 0:
                        break
                    if top >= val_a:
                        destroyed = True
                        if top == val_a:
                            stack.pop()
                        break
                    else:
                        stack.pop()
            if not destroyed:
                stack.append(a)
        return stack


def main():
    sol = Solution()
    asteroids = [5, 10, -5]
    res = sol.asteroidCollision(asteroids)
    print(res)


if __name__ == "__main__":
    main()
