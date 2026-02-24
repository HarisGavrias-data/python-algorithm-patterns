"""
Problem: Minimum Number of Arrows to Burst Balloons

You are given a list of intervals where each interval represents a balloon.
Each balloon spans from start to end on a horizontal axis.

An arrow shot at position x bursts all balloons whose interval contains x.

Return the minimum number of arrows required to burst all balloons.

Example:
Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2

Approach:
Greedy algorithm.
Sort balloons by ending coordinate and always shoot the arrow at the end
of the earliest finishing balloon. Shoot a new arrow only when the next
balloon starts after the current arrow position.

Time Complexity: O(n log n)  (sorting)
Space Complexity: O(1) or O(n) depending on sort implementation
"""

def minimum_arrows_burst_ballon(ballons):
    if not ballons:
        return 0
    ballons = sorted(ballons,key=lambda x:x[1])
    arrow = ballons[0][1]
    number_of_arrows = 1

    for start, end in ballons[1:]:
        if start > arrow:
            arrow = end
            number_of_arrows += 1

    return number_of_arrows
