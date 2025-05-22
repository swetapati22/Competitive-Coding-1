"""
#Time Complexity
- Overall O(logn)
#Space Complexity
-Overall heap storage: O(n) for storing all elements

# Did this code successfully run on Leetcode : This is not present in Leetcode.
# Any problem you faced while coding this : No, learned about helper functions and complete binary tree
"""
class MissingNumberFinder:
    def find_missing(self, arr):
        """
        Given a sorted array arr of n-1 integers in the range 1 to n,
        find the missing integer.
        
        :param arr: List[int] - sorted array of n-1 integers
        :return: int - the missing integer
        """
        #Implement your solution here:
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == mid+1:
                left = mid+1
            else:
                right = mid-1
        return left+1

def main():
    finder = MissingNumberFinder()
    
    test_cases = [
        ([1, 2, 3, 4, 6, 7, 8], 5),
        ([1, 2, 3, 4, 5, 6, 8, 9], 7),
    ]
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        result = finder.find_missing(arr)
        print(f"Test case {i}: Expected = {expected}, Got = {result}")
        assert result == expected, f"Test case {i} failed!"

if __name__ == "__main__":
    main()
