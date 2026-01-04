
"""
实验一：端口扫描模拟实验
用途：触发 Suricata 端口扫描 / 网络扫描规则
"""

import socket
import time
from datetime import datetime

TARGET_IP = "192.168.10.100"     # 被扫描主机 IP（实验区 / 管理区）
START_PORT = 20
END_PORT = 1024
TIMEOUT = 0.3                   # socket 超时时间
DELAY = 0.01                    # 每次扫描的延迟（越小越像扫描）

def scan_port(ip, port):
    """
    尝试连接指定端口
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    try:
        s.connect((ip, port))
        print(f"[+] {ip}:{port} OPEN")
        s.close()
    except (socket.timeout, ConnectionRefusedError, OSError):
        pass
    finally:
        s.close()

def main():
    print("=" * 60)
    print(" Python 端口扫描模拟实验")
    print(f" Target Host : {TARGET_IP}")
    print(f" Port Range  : {START_PORT}-{END_PORT}")
    print(f" Start Time  : {datetime.now()}")
    print("=" * 60)

    for port in range(START_PORT, END_PORT + 1):
        scan_port(TARGET_IP, port)
        time.sleep(DELAY)

    print("=" * 60)
    print(" 扫描结束")
    print(f" End Time    : {datetime.now()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
