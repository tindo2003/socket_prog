from typing import List
from collections import defaultdict
class LockingTree:

    def __init__(self, parent: List[int]):
        self.locked = set()
        self.locker = defaultdict(set) # node -> [list of user]
        self.parent = parent
        self.descendant = defaultdict(list)
        for child, parent in enumerate(self.parent):
            self.descendant[parent].append(child)

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked.add(num)
            self.locker[num].add(user)
            return True 
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locker:
            list_of_users = self.locker[num]
            if user in list_of_users:
                self.locked.remove(num)
                list_of_users.remove(user)
                return True 
            return False 
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def check_unlocked_ancestors():
            cur = num
            while cur != -1:
                if cur in self.locked:
                    return False 
                cur = self.parent[cur]
            return True
        
        def check_unlock_descendant():
            unlocked_once = False
            cur = num
            q = [cur]
            visited = set()
            while q:
                cur_node = q.pop(0)
                for child in self.descendant[cur_node]:
                    if child not in visited:
                        if child in self.locked:
                            unlocked_once = True
                        q.append(child)
                        visited.add(child)
            if not unlocked_once: return False
            return True
        
        def unlock_descendants():
            cur = num
            q = [cur]
            visited = set()
            while q:
                cur_node = q.pop(0)
                for child in self.descendant[cur_node]:
                    if child not in visited:
                        if child in self.locked:
                            self.locked.remove(child)
                            del self.locker[child]
                        q.append(child)
                        visited.add(child)
                        
        cond3 = check_unlocked_ancestors() 
        cond2 = check_unlock_descendant()
        cond1 = num not in self.locked
        
        if cond3 and cond2 and cond1:
            self.locked.add(num)
            self.locker[num].add(user)
            unlock_descendants()
            return True
        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user