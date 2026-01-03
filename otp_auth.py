import time
import hmac
import hashlib

def generate_otp(secret: str) -> str:
    """生成 6 位动态口令"""
    time_step = int(time.time()) // 30
    msg = str(time_step).encode()
    key = secret.encode()
    h = hmac.new(key, msg, hashlib.sha1).hexdigest()
    return h[:6]

def verify_otp(input_otp: str, secret: str) -> bool:
    """验证动态口令"""
    return input_otp == generate_otp(secret)
