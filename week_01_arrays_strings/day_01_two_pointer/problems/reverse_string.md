# 🔄 Reverse String

## Problem Statement
Write a function that reverses a string in-place. The input string is given as an array of characters `s`.

### Examples
```python
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

### Constraints
- 1 <= s.length <= 10^5
- `s[i]` is a printable ASCII character
- Do not allocate extra space for another array, modify the input array in-place with O(1) extra memory

## 🎯 Visual Approach

### Example Walkthrough
```
Initial: ["h", "e", "l", "l", "o"]
         ↑               ↑
        left           right

Step 1: Swap 'h' and 'o'
        ["o", "e", "l", "l", "h"]
            ↑        ↑
          left    right

Step 2: Swap 'e' and 'l'
        ["o", "l", "l", "e", "h"]
               ↑  
            (pointers meet or cross)
```

### Key Points
- Must modify the input array in-place
- Use two pointers starting from both ends
- Swap characters until pointers meet in the middle
- O(n) time complexity, O(1) space complexity

## 💡 Hints
1. Think about how you would swap two variables
2. What's the condition to stop swapping?
3. What happens with strings of even vs. odd length?
