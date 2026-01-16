import pytest
from password import check_password_strength

def test_valid_password():
    """Scenario 1: Correct password containing all required elements."""
    assert check_password_strength("A8.a") == True

def test_missing_elements():
    """Scenario 2: Passwords missing one of the required elements."""
    assert check_password_strength("aaa123.") == False
    assert check_password_strength("AAA123.") == False
    assert check_password_strength("Aa.") == False 
    assert check_password_strength("Aa123") == False

def test_invalid_characters():
    """Scenario 3: Passwords containing characters not in our allowed set (like spaces)."""
    assert check_password_strength("Aa 123.") == False