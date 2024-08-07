#include <stdio.h>
#include "tree.h"
#include <math.h>

int maxPathSumHelper(struct TreeNode* cur, int* res) {
  if (cur->left == NULL && cur->right == NULL) {
    if (cur->val > *res) {
      *res = cur->val;
    }
    return cur->val;    
  }
  int left = 0;
  int right = 0;
  if (cur->left != NULL) {
    left = maxPathSumHelper(cur->left, res);
  }
  if (cur->right != NULL) {
    right = maxPathSumHelper(cur->right, res); 
  }
  if (left < 0)
    left = 0;
  if (right < 0) 
    right = 0;
  if (left + right + cur->val > *res){
    *res = left + right + cur->val; 
  }

  return left > right ? cur->val + left : cur->val + right;
}
int maxPathSum(struct TreeNode* root) {
  int res = -INFINITY;
  maxPathSumHelper(root, &res);
  return res;
}