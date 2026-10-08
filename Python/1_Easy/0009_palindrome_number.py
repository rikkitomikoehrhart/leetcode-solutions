"""
0009. Palindrome Number
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-number/

The Problem:
    I am given an integer (x) determine if it is a palindrome (t)
    or not (f).

My Approach:
    First I converted x into a backwards string
    Second I compared a string version of x to backwards
    And returned True if it matched or False if it didn't

My Takeaway:
    There are things I forgot about Python, like that the
    reversed() function does not return a clean string. 
    Eventually I figured it out. 
    This would be a nice one to come back to in order to
    try again but without converting x to string and keeping
    it an int.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        backwards = "".join(reversed(str(x)))

        if str(x) == backwards:
            return True
        else:
            return False