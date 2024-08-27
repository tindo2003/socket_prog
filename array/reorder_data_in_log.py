from typing import List 
class Item:
    def __init__(self, identifier, content, actual_content):
        self.identifier = identifier
        self.content = content 
        self.actual_content = actual_content 
    def __lt__(self, other):
        if self.content == other.content:
            return self.identifier < other.identifier 
        else:
            return self.content < other.content 

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digits.append(log)
            else:
                letters.append(Item(identifier, rest, log))
        letters.sort()
        return [item.actual_content for item in letters] + digits

