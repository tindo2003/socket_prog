from collections import deque
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.extra = deque([])
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.extra:
            return self.extra[0]
        tmp = self.iterator.next()
        self.extra.append(tmp)
        return tmp
        

    def next(self):
        """
        :rtype: int
        """
        if self.extra:
            return self.extra.popleft()
        return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.extra) > 0 or self.iterator.hasNext()