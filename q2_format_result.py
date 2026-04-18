def format_result(value):
    """Format numeric result: integer if whole, else 4 decimal places."""
    if value == int(value):
        return str(int(value))
    return str(round(value, 4))