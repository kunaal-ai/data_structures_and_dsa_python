# ✅ Valid Palindrome

## Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples
```python
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Constraints
- 1 <= s.length <= 2 * 10^5
- `s` consists only of printable ASCII characters

## 🎯 Visual Approach

### Example Walkthrough
```
Input: "A man, a plan, a canal: Panama"

1. Clean: "amanaplanacanalpanama"
2. Two pointers:
   a m a n a p l a n a c a n a l p a n a m a
   ↑                                   ↑
   left                             right
   
   Move inwards while characters match...
```

### Key Points
- Only alphanumeric characters matter
- Case-insensitive comparison
- Empty string is a valid palindrome
- Single character is a valid palindrome
- O(n) time complexity, O(1) space complexity

## 💡 Hints
1. How can you efficiently check if a character is alphanumeric?
2. What's the base case for a palindrome?
3. How would you handle case sensitivity?
