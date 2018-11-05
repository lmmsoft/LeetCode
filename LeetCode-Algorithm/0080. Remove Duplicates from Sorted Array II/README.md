## 0080. Remove Duplicates from Sorted Array II(Medium)

[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Description
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

## Soultion
- 第26题的进化版，增加判断就行
- 常规的判断方法是: 添加到尾部的条件: 数字不重复 或者 数字重复但是之前只有一个
- 比较好，减少常数时间的判断方法是: 
    - 不需要和前第一个数比较，只有和前面第二个数比较
    - 如果不同就可以添加到尾部(最坏情况就是前面两个都相同嘛)
    - 如果相同就不能添加到尾部（因为数字是递增的，相同代表连续三个都一样）
