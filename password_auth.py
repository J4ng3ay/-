import hashlib

def hash_password(password: str) -> str:
    """对密码进行 SHA-256 哈希"""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def verify_password(input_pwd: str, stored_hash: str) -> bool:
    """验证输入密码是否正确"""
    return hash_password(input_pwd) == stored_hash
