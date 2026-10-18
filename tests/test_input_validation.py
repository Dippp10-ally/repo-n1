import pytest

from src.input_validation import require_non_empty


def test_rejects_empty_string():
    with pytest.raises(ValueError):
        require_non_empty("")


def test_rejects_whitespace_only():
    with pytest.raises(ValueError):
        require_non_empty("   ")


def test_returns_trimmed_text():
    assert require_non_empty("  hello  ") == "hello"


def test_rejects_non_string_input():
    with pytest.raises(TypeError):
        require_non_empty(None)
