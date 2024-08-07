#include "linkedlist.h"
#include <stdio.h>
#include <stdbool.h>


bool hasCycle(struct ListNode *head) {
  if (head == NULL) {
    return false;
  }
  // main trick
  struct ListNode* fast = head->next;
  struct ListNode* slow = head;

  while (fast != NULL && fast->next != NULL) {
    if (fast == slow) {
      return true;
    }
    fast = fast->next->next;
    slow = slow->next;
  }
  return false;
}