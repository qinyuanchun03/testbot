import smtplib
from email.mime.text import MIMEText

def send_test_email(sender_email, sender_password, receiver_email):
    """
    发送测试邮件

    Args:
        sender_email: 发件人邮箱地址
        sender_password: 发件人邮箱密码
        receiver_email: 收件人邮箱地址
    """

    # 构造邮件内容
    message = MIMEText("成功绑定邮箱")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "test"

    try:
        # 连接到SMTP服务器
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # 使用Gmail的SMTP服务器
            server.login(sender_email, sender_password)  # 登录邮箱
            server.sendmail(sender_email, receiver_email, message.as_string())  # 发送邮件
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败：{e}")

if __name__ == "__main__":
    sender_email = input("请输入发件人邮箱地址：")
    sender_password = input("请输入发件人邮箱密码：")
    receiver_email = input("请输入收件人邮箱地址：")

    send_test_email(sender_email, sender_password, receiver_email)
