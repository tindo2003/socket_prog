from collections import deque
def predictPartyVictory(self, senate: str) -> str:
    queue = deque(senate)
    changed = True
    while len(queue) > 1 and changed:
        top_queue = queue[0]
        if top_queue == "R":
            try:
                next_pos = queue.index("D")
                changed = True
            except ValueError:
                changed = False
                continue
        else:
            try:
                next_pos = queue.index("R")
                changed = True
            except ValueError:
                changed = False
                continue
        del queue[next_pos]
        queue.popleft()
        queue.append(top_queue)
    member = queue[0]
    if member == "R": return "Radiant"
    else: return "Dire"
        