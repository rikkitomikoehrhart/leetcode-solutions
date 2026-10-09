"""
0014. Longest Common Prefix
Difficulty: Easy
Link: https://leetcode.com/problems/longest-common-prefix

The Problem:
    Find the longest common prefix among an array of strings

My Approach:
    I sorted the list so the shortest word would be first
    because the longest common prefix couldn't be longer
    than the shortest word.

    Then I looped through the letters of that word and for
    each iteration I went through a while loop that checked
    if the letters matched, if they did, they added a counter
    to the match variable, then at the end of the loop if the 
    matched variable equaled the amount of words, then the 
    letter matched, otherwise break the loop because there is 
    no additional matches.

My Takeaway:
    This was a fun little puzzle, I feel myself getting back
    into the swing of coding.

    I think once I learn more about BigO and time complexity
    it might be nice to come back and redo all these beginning
    problems to improve my code.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""

        words = sorted(strs, key=len)
        words_length = len(words)

        for i in range(len(words[0])):
            index = 1
            match = 1
            while index < words_length:
                if (words[0][i] == words[index][i]):
                    match += 1
                index += 1
            
            if (match == words_length):
                result += words[0][i]
            else:
                break
        
        return result