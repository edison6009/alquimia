def exist(value):
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    return value