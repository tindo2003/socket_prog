#include "tree/tree.h"
#include <stdio.h>

int helper(struct TreeNode* cur, int* sum) {
  if (cur == NULL) {
    return 1;
  }
  int leftRes = helper(cur->left, sum);
  int rightRes = helper(cur->right, sum);
  if (leftRes == 0 || rightRes == 0) {
    *sum = *sum + 1;
    return 2;
  } else if (leftRes == 2 || rightRes == 2) {
    return 1;
  } else {
    return 0;
  }
  return 0;
}

int minCameraCover(struct TreeNode* root) {
  /* 
  * 0: not monitored
  * 1: monitored
  * 2: has camera
  */
  int sum = 0;
  if (helper(root, &sum) == 0)
    sum++;
  return sum;
}