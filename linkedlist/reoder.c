#include "linkedlist.h"
#include <stdio.h>

struct ListNode* find_middle(struct ListNode* head);
struct ListNode* reverse(struct ListNode* head);

void reorderList(struct ListNode* head) {
  struct ListNode* middle = find_middle(head);
  struct ListNode* right = reverse(middle->next);
  middle->next = NULL;
  struct ListNode* left = head;
  struct ListNode* next = NULL;
  while (left != NULL && right != NULL) {
    next = left->next;
    left->next = right;
    right = right->next;
    left = left->next;
    left->next = next;
    left = left->next;
  }
    
}

struct ListNode* find_middle(struct ListNode* head) {
  struct ListNode* slow = head;
  struct ListNode* fast = head;

  while (fast->next != NULL && fast->next->next != NULL) {
    fast = fast->next->next;
    slow = slow->next; 
  }
  return slow;
}

struct ListNode* reverse(struct ListNode* head) {
  struct ListNode* prev = NULL;
  struct ListNode* next = NULL;
  struct ListNode* cur = head; 

  while (cur != NULL) {
    next = cur->next;
    cur->next = prev;
    prev = cur;
    cur = next;
  }
  return prev->next;
}

