#!/usr/bin/env python3
"""
Test hello query
"""
import pytest
from hello import hello

test_cases = [
    (3, "Hello, World! 3")
]

@pytest.mark.parametrize("number,matches", test_cases)
def test_hello(number, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert hello(number) == matches
