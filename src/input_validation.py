"""Reusable validation for required text values."""


def require_non_empty(value, field_name="value"):
    """Return stripped text or raise ValueError for blank input."""
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")

    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} must not be empty")

    return cleaned
