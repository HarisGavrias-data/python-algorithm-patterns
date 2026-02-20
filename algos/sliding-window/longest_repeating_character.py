"""
Problem: Longest Substring Without Repeating Characters
Pattern: Sliding Window
Difficulty: Medium

Description:
Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within the string.

Constraints:
- 0 ≤ len(s) ≤ 50,000
- s consists of English letters, digits, symbols, and spaces.

Return:
An integer representing the length of the longest substring without duplicate characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters.

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
Explanation: "wke" is the longest substring without repeating characters.
"""
def longest_sub_without_repeating(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best
