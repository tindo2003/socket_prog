
def tmp(n:int) -> int:
    cur = 1
    copied = 0 
    ans = 0

    while cur != n:
        if (n - cur) % cur == 0:
            copied = cur 
            ans += 2
        else:
            ans += 1
        cur += copied
    return ans