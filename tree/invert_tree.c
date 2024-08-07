#include "tree.h"
#include <stdio.h>

void invertTree_rec(struct TreeNode* cur) {
  if (cur == NULL) {
    return;
  }
  struct TreeNode* tmp = cur->left;
  cur->left = cur->right;
  cur->right = tmp;

  if (cur->left != NULL) {
    invertTree_rec(cur->left);
  } 

  if (cur->right != NULL) {
    invertTree_rec(cur->right);
  }
} 

struct TreeNode* invertTree(struct TreeNode* root) {
  invertTree_rec(root);
  return root;
}
