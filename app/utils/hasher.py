import bcrypt

class PasswordHasher:
    def toHash(password: str) -> str:
        salt = bcrypt.gensalt(16)
        print(salt)
        return bcrypt.hashpw(password.encode("utf-8"), salt)
    
    def compare(hashed: str, password: str) -> bool:
        return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password= hashed)