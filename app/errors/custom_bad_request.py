from werkzeug.exceptions import BadRequest
from typing import Optional
from flask import Response


class FormInputError:
    def __init__(self, key: str, reason: str, hint: Optional[str] = None) -> None:
        self.key = key
        self.reason = reason
        self.hint = hint

    def serialize(self) -> dict[str, any]:
        return {
            "key": self.key,
            "reason": self.reason,
            "hint": self.hint
        }
    
    def __repr__(self) -> str:
        hint = f" to avoid it try {self.hint}" if hint is not None else ""
        return f"[in key:{self.key} an error occurred because {self.reason}.{self.hint}]"
    

    

class InvalidFormData(Exception):
    def __init__(self, inputErrors: list[FormInputError], message: Optional[str] = None) -> None:
        self.message = message
        self.inputErrors = inputErrors
        super().__init__(message)

    def serialize(self) -> dict[str, any]:
        return {
            "message": self.message,
            "details": [
                error.serialize()
                for error in self.inputErrors
            ],
        }