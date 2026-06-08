# Assignment 165: Compare Version Numbers

Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. 
The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. 
If one of the version strings has fewer revisions, treat the missing revision values as 0.
Return the following:
    - If version1 < version2, return -1.
    - If version1 > version2, return 1.
    - Otherwise, Return 0 

Example 1:
    - Input: version1 = "1.2", version2 = "1.10"
    - Output: -1
    - Explaination: version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
    - Input: version1 = "1.01", version2 = "1.001"
    - Output: 0
