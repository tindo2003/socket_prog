#include <stdio.h>
#include "tree.h"

struct TreeNode* helper(struct TreeNode* cur, struct TreeNode* p, struct TreeNode* q) {
  if (cur->left == NULL && cur->right == NULL) {
    if (cur == p) {
      return p;
    }
    if (cur == q) {
      return q;
    } 
  }

  struct TreeNode* left = NULL;
  struct TreeNode* right = NULL;
  if (cur->left != NULL) {
    left = helper(cur->left, p, q);
  }
  if (cur->right != NULL) {
    right = helper(cur->right, p, q); 
  }
  if (left != NULL && right != NULL) {
    return cur;
  } else if (left != NULL) {
    if (left == p && cur == q) {
      return cur;
    }
    if (left == q && cur == p) {
      return cur;
    }
    return left;
  } else if (right != NULL) {
    if (right == p && cur == q) {
      return cur;
    }
    if (right == q && cur == p) {
      return cur;
    }
    return right;
  }
  if (cur == p || cur == q) {
    return cur;
  }
  return NULL;
}


struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
  struct TreeNode* tmp = helper(root, p, q);
  return tmp;
}