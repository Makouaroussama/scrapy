import bcrypt

class PasswordHasher:
    def toHash(password: str) -> str:
        salt = bcrypt.gensalt(12)
        return bcrypt.hashpw(password.encode("utf-8"), salt)
    
    def compare(hashed: str, password: str) -> bool:
        return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password= hashed)