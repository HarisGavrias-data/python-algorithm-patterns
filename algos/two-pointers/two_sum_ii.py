"""
Problem: Two Sum II (Sorted Array)
Pattern: Two Pointers
Difficulty: Easy–Medium

Description:
Given a 0-indexed sorted array of integers `numbers` and an integer `target`,
return the indices of the two numbers such that they add up to `target`.

Constraints:
- The array is sorted in non-decreasing order.
- Exactly one solution exists.
- You may not use the same element twice.
- You must use constant extra space.

Return:
A tuple containing the two indices of the numbers that sum to target.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: (0, 1)
"""
def sum_target_sorted_array(nums,target):
    if not nums:
        return None
    left = 0
    right = len(nums) - 1
    while left < right:
        checker = nums[left] + nums[right]
        if checker == target:
            return left,right
        elif checker > target:
            right -= 1
        else:
            left += 1
    
