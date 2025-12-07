"""
Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Find two numbers in the array that sum up to the target.
    
    Args:
        numbers: A list of integers sorted in non-decreasing order.
        target: The target sum to find.
        
    Returns:
        A list containing the 1-based indices of the two numbers that sum to the target.
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [1, 2]
        >>> two_sum([2, 3, 4], 6)
        [1, 3]
    """
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            # Return 1-based indices
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def test_two_sum():
    """Test cases for the two_sum function."""
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 5], 9, [4, 5]),
        ([1, 1], 2, [1, 2]),
    ]
    
    for numbers, target, expected in test_cases:
        result = two_sum(numbers, target)
        assert result == expected, f"Failed for input {numbers} with target {target}. Expected {expected}, got {result}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_two_sum()
