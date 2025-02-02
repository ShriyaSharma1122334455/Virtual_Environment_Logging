"""This module contains calculator functions."""

from calculator import add, substract

def test_addition():
    """Tests that add() correctly adds two numbers."""
    assert add(2, 2) == 4

def test_substraction():
    """Tests that add() correctly adds two numbers."""
    assert substract(2, 2) == 0

# Ensure the file ends with a newline
