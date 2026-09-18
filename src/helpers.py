# Build: 5f8ad5b62ce3081b3be6de4aeccbcdc5

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
