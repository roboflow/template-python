"""Test the hello module."""

from sandbox.hello import hello


def test_hello():
    """Test the hello function."""
    res = hello()
    assert res == "World"
