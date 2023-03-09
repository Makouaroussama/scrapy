from app.models.user import User
from datetime import datetime

class UserRepository:
    async def exists(id: str, email: str) -> bool:
        if id==None and email==None: 
            return False
    
    async def getUserById(id: str) -> User | None:
        return None
    
    async def getUserByEmail(email: str, test: bool) -> User | None:
        if(test):
            return User("5f37e1f8-56cb-41b7-b87a-aa0892e749ef", "makouar@gmail.com", "secretly_preserved", datetime.now())
        return None;

    async def save(user: User) -> User:
        pass;
