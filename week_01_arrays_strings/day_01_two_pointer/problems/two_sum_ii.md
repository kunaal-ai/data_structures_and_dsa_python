# Two Sum II - Input Array Is Sorted

## Problem Statement
Given a 1-indexed array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `[index1, index2]` as an integer array `[index1, index2]` of length 2.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

### Examples
```python
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].
```

### Constraints
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.

## 🔍 Visual Approach

```
Array: [2, 7, 11, 15], Target: 9

Step 1: 2 + 15 = 17 > 9 → Move right pointer
        ↑        ↑
       left    right

Step 2: 2 + 11 = 13 > 9 → Move right pointer
        ↑     ↑
       left  right

Step 3: 2 + 7 = 9 → Found! Return [1,2]
        ↑  ↑
      left right
```

### Key Points:
- Array must be sorted
- Left starts at beginning, right at end
- Move right if sum > target
- Move left if sum < target
- O(n) time, O(1) space



### Complexity Analysis
- **Time Complexity**: O(n), where n is the number of elements in the array. In the worst case, we might need to check all elements once.
- **Space Complexity**: O(1), as we are using a constant amount of extra space.

## Follow-up Questions
1. How would you modify the solution if the input array is not sorted?
2. What if there are multiple pairs that sum up to the target? How would you handle that?
3. How would you optimize the solution for very large input sizes?

## Additional Notes
- The two-pointer technique is efficient here because the array is sorted.
- This approach ensures that we only need to traverse the array once, making it optimal for this problem.
