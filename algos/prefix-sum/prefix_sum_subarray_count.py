# Problem: Subarray Sum Equals K
#
# Given an integer array `nums` and an integer `k`, return the total number
# of continuous subarrays whose sum equals `k`.
#
# Approach:
# Used prefix sums and a hashmap to count occurrences efficiently.

def subarray_sum(nums, k):
    prefix_count = {0: 1}
    prefix = 0
    ans = 0

    for x in nums:
        prefix += x

        if prefix - k in prefix_count:
            ans += prefix_count[prefix - k]

        
        prefix_count[prefix] = prefix_count.get(prefix,0) + 1


    return ans
