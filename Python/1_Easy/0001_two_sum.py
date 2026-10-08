"""
0001. Two Sun
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

The Problem:
    I am given an integer array (nums) and a target integer (target) 
    and I am expect to return the indices of any two numbers from the 
    array that added together equal the target.

My Approach:
    First I created an empty array to hold my results
    Second I started a for loop to loop through nums
    Next I checked if target - current num in loop is in nums
    After I checked to make sure it wasn't returning itself
        (i.e. target = 6 and the first number in the array is 3
        then the result would be [0,0] which would be wrong)
    Then I appended the answers to results
    Finally I returned results

My Takeaway:
    This was a fun challenge to get back into the swing of programming.
    I spent the last year working inside CRM software and didn't get
    a lot of opportunities to code. I miss coming up with easy, readable
    solutions.

"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        results = []

        for i in range(len(nums)):
            if ((target - nums[i]) in nums):
                result = nums.index(target - nums[i])
                if (i != result):
                    results.append(i)
                    results.append(result)
                    break
        
        return results

