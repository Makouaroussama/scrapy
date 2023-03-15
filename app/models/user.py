from __future__ import annotations
from sqlalchemy_utils import UUIDType
from datetime import datetime
from app.utils.hasher import PasswordHasher
from typing import Optional
from ..db import db
from sqlalchemy.sql import func
from app.processes.decorators.validate_form import Credentials

import uuid
class User(db.Model):
    id = db.Column(UUIDType(), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128), index=True, unique=True)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, email: str, password: str, id: Optional[str] = None, createdAt: Optional[datetime] = None):
        self.id = id
        self.email = email
        self.password = PasswordHasher.toHash(password)
        self.createdAt = createdAt

    def fromCredentials(credentials: Credentials) -> User:
        return User(email=credentials.email, password=credentials.password)
        
    def isPersisted(self) -> bool:
        return self.id != None

    def isPasswordMatched(self, password: str) -> bool:
        return PasswordHasher.compare(self.password, password)

    
    def payload(self) -> dict[str, any]:
        return {
            'id': self.id.__str__(),
            'email': self.email,
        }
    
    def dto(self) -> dict[str, any]:
        return {
            **self.payload(),
            'createdAt': self.createdAt,
        }
    
    def __repr__(self) -> str:
        return f'''
            User(
                id: {self.id.__str__()},
                email: {self.email},
                password: {self.password},
                createdAt: {self.createdAt},
            )
        '''