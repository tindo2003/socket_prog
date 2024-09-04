
def find_left(nums: list[int], target):
    l = 0 
    r = len(nums) - 1
    wanted_idx = 0
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            r = mid - 1
            wanted_idx = mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return wanted_idx

def find_right(nums: list[int], target):
    l = 0 
    r = len(nums) - 1
    wanted_idx = 0
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            l = mid + 1
            wanted_idx = mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return wanted_idx
def main():
    nums = [1, 3, 4, 6, 7, 7, 7, 7, 9]
    target = 7
    res = find_left(nums, target)
    res1 = find_right(nums, target)
    print(res)
    print(res1)

if __name__ == "__main__":
    main()

