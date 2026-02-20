"""
Problem: Longest Repeating Character Replacement
Pattern: Sliding Window
Difficulty: Medium

Description:
You are given a string `s` consisting of only uppercase English letters and an integer `k`.
You may replace at most `k` characters in the string with any other uppercase letter.

Return the length of the longest substring containing the same letter you can get
after performing at most `k` replacements.

Constraints:
- 1 ≤ len(s) ≤ 100,000
- s consists only of uppercase English letters
- 0 ≤ k ≤ len(s)

Return:
An integer representing the maximum length of a substring that can be turned into all
identical characters with at most k replacements.

Examples:
Input: s = "ABAB", k = 2
Output: 4

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'A' with 'B' to get "AABBBBA".
"""
def longest_sub_without_repeating_replacement(s,k):
    seen = {}
    left = 0
    best = 0
    max_freq = 0
    for right, char in enumerate(s):
        seen[char] = seen.get(char,0) + 1
        max_freq = max(max_freq,seen[char])
        while (right - left + 1) - max_freq > k:
            seen[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
