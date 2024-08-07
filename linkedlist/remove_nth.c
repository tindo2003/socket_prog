#include "linkedlist.h"
#include <stdio.h>

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
  struct ListNode* fast = head;
  struct ListNode* slow = head;
  while (n > 0) {
    fast = fast->next;
    n--;
  }

  // remove head case
  if (fast == NULL) {
    return head->next;
  }

  if (fast != NULL && fast->next != NULL) {
    fast = fast->next;
    slow = slow->next;
  }

  if (slow != NULL && slow->next != NULL) {
    slow->next = slow->next->next;
  }

  return head;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
  int length = 0;
  struct ListNode* tmp = head;
  while (tmp != NULL) {
    length++;
    tmp = tmp->next;
  }

  struct ListNode* prev = NULL;
  struct ListNode* cur = head;
  
  for (int i = 0; i < length - n; i++) {
    prev = cur; 
    cur = cur->next;
  }

  if (cur == head) {
    // remove head
    return head->next;
  } else if (cur->next == NULL) {
    // remove tail
    prev->next = NULL;
  } else {
    prev->next = cur->next;
  }

  return head;
}