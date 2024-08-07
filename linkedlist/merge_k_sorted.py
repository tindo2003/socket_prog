#include "linkedlist.h"
#include <stdio.h>
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists):
  heap = []
  for ll in lists:
    temp = ll
    while temp:
      heapq.heappush(heap, temp.val)
      temp = temp.next
  
  dummy = ListNode()
  while (heap):
     cur_val = heapq.heappop(heap)
     dummy.next = ListNode(cur_val)
     dummy = dummy.next 
  return dummy.next