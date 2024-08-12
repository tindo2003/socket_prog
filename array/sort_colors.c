#include <stdio.h>

void sortColors(int* nums, int numsSize) {
  int num0 = 0;
  int num1 = 0;
  int num2 = 0;
  int cur_ele = 0;
  int cur_idx = 0;
  for (int i = 0; i < numsSize; i++) {
    cur_ele = nums[i];
    if (cur_ele == 0) {
      num0++;
    } else if (cur_ele == 1) {
      num1++;
    } else if (cur_ele == 2) {
      num2++;
    }
  }  
  while (num0 >= 0) {
    nums[cur_idx] = 0;
    cur_idx++;
    num0--;
  }
  while (num1 >= 0) {
    nums[cur_idx] = 1;
    cur_idx++;
    num1--;
  }
  while (num2 >= 0) {
    nums[cur_idx] = 2;
    cur_idx++;
    num2--;
  }
}