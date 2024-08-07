#include "linkedlist.h"
#include <stdio.h>

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
  struct ListNode dummy;
  struct ListNode* tmp = &dummy;

  while (list1 != NULL && list2 != NULL) {
    if (list1->val <= list2->val) {
      tmp->next = list1;
      list1 = list1->next;
    } else {
      tmp->next = list2;
      list2 = list2->next;
    }
    tmp = tmp->next;
  }

  if (list1 == NULL) {
    tmp->next = list2;
  } else {
    tmp->next = list1;
  }
  
  return dummy.next;
}