""
Node class for various data structures.

This module provides a basic Node class that can be used as a building block
for different data structures like linked lists, trees, etc.
"""
from typing import Any, Optional, TypeVar

T = TypeVar('T')

class Node:
    """A node class for linked data structures.
    
    Attributes:
        data: The data stored in the node.
        next: Reference to the next node in the sequence.
    """
    
    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        """Initialize a node with data and an optional next node reference.
        
        Args:
            data: The data to store in the node.
            next_node: Reference to the next node in the sequence. Defaults to None.
        """
        self.data = data
        self.next = next_node
    
    def __repr__(self) -> str:
        """Return a string representation of the node."""
        return f"Node(data={self.data!r}, next={'...' if self.next else 'None'})"
    
    def __eq__(self, other: object) -> bool:
        """Check if two nodes are equal based on their data and next references."""
        if not isinstance(other, Node):
            return False
        return self.data == other.data and self.next is other.next


class TreeNode:
    """A node class for binary trees.
    
    Attributes:
        val: The value stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """
    
    def __init__(
        self, 
        val: T, 
        left: Optional['TreeNode'] = None, 
        right: Optional['TreeNode'] = None
    ):
        """Initialize a tree node with a value and optional child nodes.
        
        Args:
            val: The value to store in the node.
            left: Reference to the left child node. Defaults to None.
            right: Reference to the right child node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        """Return a string representation of the tree node."""
        return f"TreeNode(val={self.val!r}, left={'...' if self.left else 'None'}, right={'...' if self.right else 'None'})"
    
    def __eq__(self, other: object) -> bool:
        """Check if two tree nodes are equal based on their values and subtrees."""
        if not isinstance(other, TreeNode):
            return False
        return (
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )
