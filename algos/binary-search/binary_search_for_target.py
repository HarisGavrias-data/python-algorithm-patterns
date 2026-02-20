"""
Problem: Binary Search
Pattern: Binary Search
Difficulty: Easy

Description:
Given an array of integers `nums` sorted in ascending order and an integer `target`,
write a function to search for `target` in `nums`.

If `target` exists, return its index.
If it does not exist, return -1.

Constraints:
- `nums` is sorted in ascending order.
- 1 ≤ len(nums) ≤ 10^4 (commonly)
- You must solve it in O(log n) time.

Examples:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
"""
def search_in_sorted_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
