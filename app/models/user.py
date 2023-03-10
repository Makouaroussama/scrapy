from app.utils.hasher import PasswordHasher
from datetime import datetime
from typing import Optional
class User:
    def __init__(self, id: str, email: str, password: str, createdAt: Optional[datetime] = None):
        self.id = id
        self.email = email
        self.password = PasswordHasher.toHash(password)
        self.createdAt = createdAt

    def isPasswordMatched(self, password: str) -> bool:
        return PasswordHasher.compare(self.password, password)

    
    def payload(self) -> dict[str, any]:
        return {
            'id': self.id,
            'email': self.email,
        }
    
    def dto(self) -> dict[str, any]:
        return {
            **self.payload(),
            'createdAt': self.createdAt,
        }
    
    def __repr__(self) -> str:
        return '''
            User(
                id: {self.id},
                email: {self.email},
                password: {self.password},
                createdAt: {self.createdAt},
            )
        '''