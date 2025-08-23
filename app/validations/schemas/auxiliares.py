import re

def has_invalid_characters(value: str) -> bool:
    return not re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+$", value)

def has_spaces(value: str) -> bool:
    return " " in value

def username_has_invalid_format(value: str) -> bool:
    return not re.match(r"^[a-zA-Z0-9_.-]+$", value)
