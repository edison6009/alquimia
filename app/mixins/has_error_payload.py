def has_error_payload(data: object) -> bool:
    """
    Verifica si el objeto 'data' es un dict que contiene campos de error estructurados.
    Retorna True si al menos uno de los campos esperados ('error', 'conflict', 'validations')
    está presente y tiene contenido tipo lista o dict.
    """

    # Si 'data' no es un diccionario, no puede tener claves relevantes → no es error payload
    if not isinstance(data, dict):
        return False

    # Recorre las claves esperadas y evalúa si alguna está presente con contenido estructurado
    return any(
        key in data and isinstance(data[key], (list, dict))  # Clave existe y tiene estructura válida
        for key in ("error", "conflict", "validations")      # Claves que indican errores en el payload
    )
