from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        pass

def main():
    sol = Solution()
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    res = sol.countStudents(students, sandwiches)
    print(res)

if __name__ == "__main__":
    main()