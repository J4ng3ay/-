from user import User
from password_auth import verify_password
from otp_auth import verify_otp, generate_otp

def authenticate(user: User):
    print("多因素身份验证系统")

    username = input("用户名：")
    if username != user.username:
        print("用户名不存在")
        return

    password = input("密码：")
    if not verify_password(password, user.password_hash):
        print("密码验证失败")
        return



    otp = input("请输入动态口令：")
    if not verify_otp(otp, user.secret):
        print("动态口令错误")
        return

    print("身份验证成功，登录通过！")

if __name__ == "__main__":
    # 创建示例用户
    user = User(
        username="sjq",
        password="123456",
        secret="ABCDEF123456"
    )

    print("系统初始化完成")
    print("当前动态口令示例（30 秒内有效）：", generate_otp(user.secret))
    print("---------------------------------")

    authenticate(user)
