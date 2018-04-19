Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

# 解决方案

1. 找到一个k,使得```nums[k]<nums[k+1]```,同时k是最大的下标

> 如果没有这样的k，表示该数列是有序的，直接逆序即可。 

2. 找到一个l,使得```nums[l]>nums[k]```,同时l也是最大的下标

3. swap

4. 对剩余的```nums[k+1:]```进行reverse