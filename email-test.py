import smtplib
from email.mime.text import MIMEText
import os
import logging

# 配置日志记录
logging.basicConfig(filename="email_test.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def send_test_email(sender_email, sender_password, receiver_email):
    # ... (邮件发送逻辑不变)

if __name__ == "__main__":
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    receiver_email = os.environ.get("RECEIVER_EMAIL")

    if not all([sender_email, sender_password, receiver_email]):
        print("请设置 SENDER_EMAIL, SENDER_PASSWORD 和 RECEIVER_EMAIL 环境变量。")
        exit(1)

    # 检查是否是第一次运行
    first_run = os.path.exists("first_run.txt")

    if not first_run:
        # 第一次运行，记录日志并退出
        logging.info("第一次运行，请在 GitHub Actions 页面手动触发工作流以启动邮件发送。")
        with open("first_run.txt", "w") as f:
            f.write("已运行")
    else:
        # 不是第一次运行，正常发送邮件
        send_test_email(sender_email, sender_password, receiver_email)
