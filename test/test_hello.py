"""Test the hello module."""

from sandbox.hello import hello


def test_hello() -> None:
    """Test the hello function."""
    res = hello()
    assert res == "World"
