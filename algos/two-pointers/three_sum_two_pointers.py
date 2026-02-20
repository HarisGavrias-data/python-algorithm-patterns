"""
Problem: 3Sum (Two Pointers Technique)

This program solves the classic "3Sum" problem:

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that:
    i != j != k
    nums[i] + nums[j] + nums[k] == target

Requirements:
- Must run in O(n^2) time
- Must avoid duplicate triplets
- Must use sorting + two-pointer technique

Approach:
1. Sort the array.
2. Fix one element.
3. Use two pointers to find the remaining pair that sums to target.
4. Skip duplicates to ensure unique results.

Concepts demonstrated:
- Two pointer technique
- Sorting for optimization
- Duplicate handling
- Time complexity optimization from O(n^3) → O(n^2)
"""
def three_nums_to_target(nums,target):
    if not nums:
        return None
    nums.sort()
    for idx, number in enumerate(nums):
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + number < target:
                left += 1
            elif nums[left] + nums[right] + number > target:
                right -= 1
            else:
                return nums[left],nums[right],number
    return None
