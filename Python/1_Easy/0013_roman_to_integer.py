"""
0013. Roman to Integer
Difficulty: Easy
Link: https://leetcode.com/problems/roman-to-integer

The Problem:
    Convert a roman numeral into an integer

My Approach:
    I decided the easiest way would be to loop through
    and if the roman number after it is larger then 
    subtract the current number, if the number after
    is smaller, add it.

My Takeaway:
    It may not be the most efficient, but I think this 
    worked nicely and did the job. 

    I would like to come back to this later and see 
    where I can improve it. 

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        romans = list(s)

        mapping = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        numbers = [mapping[item] for item in romans]

        for i in range(len(numbers)):
            if (i != len(numbers)-1):
                if (numbers[i] < numbers[i+1]):
                    total -= numbers[i]
                else:
                    total += numbers[i]
            else:
                total += numbers[i]

        return total