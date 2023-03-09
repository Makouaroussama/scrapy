from models.user import User


class UserRepository:
    async def exists(id: str, email: str) -> bool:
        if id==None and email==None: 
            return False
        
        
    
    async def getUserById(id: str) -> User | None:
        return None
    
    async def getUserByEmail(email: str) -> User | None:
        return None;

    async def save(user: User) -> User:
        pass;
