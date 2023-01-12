"""
description:https://leetcode.com/problems/two-sum/description/
sample solution:https://leetcode.com/problems/two-sum/solutions/2361743/python-simple-solution-o-n-time-o-n-space/
"""

"""
my slolution
"""
class Solution:
    def twoSum(self, nums, target):
        for k in nums:
            nums_new = nums[:]
            v = target - k
            nums_new.remove(k)
            if v in nums_new:
                ki = nums.index(k)
                kv = nums_new.index(v) + 1
                return ([ki, kv])



