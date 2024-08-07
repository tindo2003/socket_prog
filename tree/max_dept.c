#include <stdio.h>
#include "tree.h"

int maxDepth_rec(struct TreeNode* cur) {
  if (cur == NULL) {
    return 0;
  }
  int left_sum = 1 + maxDepth_rec(cur->left);
  int right_sum = 1 + maxDepth_rec(cur->right);
  if (left_sum > right_sum) {
    return left_sum;
  } else {
    return right_sum;
  }
}
int maxDepth(struct TreeNode* root) {
  return maxDepth_rec(root); 
}