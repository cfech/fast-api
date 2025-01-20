from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes="bcrypt", deprecated = "auto")

class Hash():
    def bcrypt(password: str):
        return pwd_ctx.hash(password)
    
    def verify(hash_password: str, plain_password: str):
        return pwd_ctx.verify(hash_password, plain_password)