from pydantic import BaseModel, ValidationError
from pydantic_core import ErrorDetails

class MultiError(Exception):
    def __init__(self, field: str, messages: list[str]):
        self.field = field
        self.messages = messages

    def to_error_details(self) -> list[ErrorDetails]:
        return [
            ErrorDetails(
                type='value_error',
                loc=(self.field,),
                msg=msg,
                input=None
            )
            for msg in self.messages
        ]


