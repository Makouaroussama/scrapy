


class Credentials:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password


    def serialize(self)-> dict[str, any]:
        return {
            "email": self.email,
            "password": self.password
        }