"""
🔄 Reverse String

Write a function that reverses a string in-place.
The input string is given as an array of characters s.

Example:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def reverse_string(s: list[str]) -> None:
    """
    Reverse the string in-place using two pointers.
    
    Args:
        s: List of characters to be reversed in-place
        
    Returns:
        None (modifies the input list in-place)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters
        s[left], s[right] = s[right], s[left]
        # Move pointers towards center
        left += 1
        right -= 1

def test_reverse_string():
    """Test cases for reverse_string function."""
    test_cases = [
        (["h","e","l","l","o"], ["o","l","l","e","h"]),
        ("Hannah".split(), list("hannaH")),
        (["A"], ["A"]),
        (list("racecar"), list("racecar")),
        (list("hello world"), list("dlrow olleh"))
    ]
    
    print("\n" + "="*50)
    print("🔄 Testing Reverse String")
    print("="*50)
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        # Create a copy since we're modifying in-place
        s = input_str.copy()
        reverse_string(s)
        status = "✅ PASS" if s == expected else "❌ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Input:    {input_str}")
        print(f"Expected: {expected}")
        print(f"Got:      {s}")
    
    print("\n" + "="*50)
    print("✨ Testing Complete!")

if __name__ == "__main__":
    test_reverse_string()
