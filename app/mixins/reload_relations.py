from settings import SessionLocal
from sqlalchemy.orm import selectinload

def reload(obj, *rels):
    # Recarga una instancia desacoplada desde la base de datos, incluyendo relaciones especificadas.
    # Valida que cada relación exista en el modelo antes de aplicar selectinload.

    cls = obj.__class__
    # Obtiene la clase del objeto para construir la consulta sin hardcodear el modelo.

    invalid = [r for r in rels if not hasattr(cls, r)]
    # Verifica que cada relación solicitada exista como atributo en el modelo.
    # Si alguna no existe, se acumula en la lista `invalid`.

    if invalid:
        raise AttributeError(f"Relaciones no válidas en {cls.__name__}: {invalid}")
        # Si hay relaciones inválidas, se lanza una excepción explícita con detalles.

    with SessionLocal() as s:
        # Abre una sesión temporal para realizar la consulta de forma segura.

        return (
            s.query(cls)
            .options(*[selectinload(getattr(cls, r)) for r in rels])
            .get(obj.id)
        )
        # Realiza la consulta por ID, aplicando selectinload a cada relación válida.
        # selectinload evita N+1 queries y permite cargar múltiples relaciones eficientemente.
        # getattr(cls, r) accede dinámicamente a los atributos relacionales del modelo.




#uso: user = reload(user, "posts", "profile", "settings")

