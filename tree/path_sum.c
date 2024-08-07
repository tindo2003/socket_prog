#include "tree.h"
#include <stdio.h>
#include <stdbool.h>

bool helper(struct TreeNode* cur, int curSum) {
  // leaf condition
  if (cur->left == NULL && cur->right == NULL) {
    return (curSum - cur->val) == 0;
  }
  bool left = false;
  bool right = false;
  if (cur->left != NULL) {
    left = helper(cur->left, curSum - cur->val);
  }
  if (cur->right != NULL) {
    right = helper(cur->right, curSum - cur->val);
  }
  
  if (left == true || right == true) {
    return true;
  }
  return false;
}

bool hasPathSum(struct TreeNode* root, int targetSum) {
    if (root == NULL) 
        return false;
    return helper(root, targetSum);
}

