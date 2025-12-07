"""
✅ Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.

Example:
Input: "A man, a plan, a canal: Panama"
Output: true
"""

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a valid palindrome using two pointers.
    
    Args:
        s: Input string to check
        
    Returns:
        bool: True if the string is a valid palindrome, False otherwise
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare characters case-insensitively
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

def test_is_palindrome():
    """Test cases for is_palindrome function."""
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),  # Empty string is a valid palindrome
        ("a.", True),  # Single character is a valid palindrome
        ("0P", False),  # Edge case with numbers and letters
        ("Able was I, I saw elba", True),
        ("race a car", False)
    ]
    
    print("\n" + "="*50)
    print("✅ Testing Valid Palindrome")
    print("="*50)
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_palindrome(input_str)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"Input:    {input_str}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
    
    print("\n" + "="*50)
    print("✨ Testing Complete!")

if __name__ == "__main__":
    test_is_palindrome()
