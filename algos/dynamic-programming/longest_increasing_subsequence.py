"""
Problem: Longest Increasing Subsequence (LIS)

Given an integer array `nums`, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence derived from an array by deleting some or no
elements without changing the order of the remaining elements.

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation:
One longest increasing subsequence is [2,3,7,101].

Approach:

Dynamic Programming (O(n^2)):
- dp[i] represents the length of the longest increasing subsequence ending at i.


Time Complexity:
- DP approach: O(n^2)


Space Complexity: O(n)
"""
def lis_length_dp(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                candidate = dp[j] + 1
                if candidate > dp[i]:
                    dp[i] = candidate

    return max(dp)
