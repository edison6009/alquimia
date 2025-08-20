from pydantic import ValidationError
import re

def formats_validations(e: ValidationError) -> dict[str, list[str]]:
    # Transforma un ValidationError de Pydantic en un dict con listas de errores por campo

    errors: dict[str, list[str]] = {}
    # Diccionario acumulador: clave = nombre del campo, valor = lista de mensajes de error

    for err in e.errors():
        field = err["loc"][0]
        # Extrae el nombre del campo afectado desde la ubicación del error

        raw_msg = err["msg"]
        # Obtiene el mensaje de error original generado por Pydantic

        # Elimina prefijos como "Value error, " si existen, para limpiar el mensaje
        if ", " in raw_msg:
            raw_msg = raw_msg.split(", ", 1)[1]

        # Divide el mensaje en partes si contiene múltiples errores concatenados
        split_msgs = [msg.strip() for msg in re.split(r"[.,]", raw_msg) if msg.strip()]
        # Se eliminan espacios y se descartan fragmentos vacíos

        errors.setdefault(field, []).extend(split_msgs)
        # Acumula los mensajes en una lista por campo, respetando el formato esperado

    return errors
    # Devuelve el dict final con errores estructurados por campo
