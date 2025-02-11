import os
import requests
import datetime

# 从环境变量中获取机器人 token 和用户信息
BOT_TOKEN = os.environ.get("BOT_TOKEN")
USER_ID = os.environ.get("USER_ID")
FIRST_NAME = os.environ.get("FIRST_NAME")
LAST_NAME = os.environ.get("LAST_NAME")
LANG = os.environ.get("LANG")

def send_message(message):
  """发送消息到 Telegram"""
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  data = {
      "chat_id": USER_ID,
      "text": message
  }
  response = requests.post(url, json=data)
  return response.json()

def schedule_message(message, time):
  """
  调度消息发送
  Args:
    message: 要发送的消息
    time: 消息发送时间，格式为 YYYY-MM-DD HH:MM:SS
  """
  now = datetime.datetime.now()
  scheduled_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

  if scheduled_time <= now:
    send_message(message)
    return

  delay = (scheduled_time - now).total_seconds()
  print(f"Message scheduled in {delay} seconds...")

  # 在 GitHub Actions 中，无法使用 time.sleep() 进行长时间等待
  # 因此，我们需要将任务交给 GitHub Actions 的定时任务来执行

def main():
  message = "Hello, this is a scheduled message!"
  time = "2023-12-31 23:59:59"  # 设置消息发送时间

  schedule_message(message, time)

if __name__ == "__main__":
  main()
