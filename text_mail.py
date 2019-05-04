import smtplib
from email import message

import config

# 基本情報
smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = config.from_email
to_email = config.to_email
username = config.username
password = config.password

# メール
msg = message.EmailMessage()
msg.set_content("テストメールです")
msg['Subject'] = "テストメールの件名です。"
msg["From"] = from_email
msg["To"] = to_email

# サーバインスタンス作成
server = smtplib.SMTP(host=smtp_host, port=smtp_port)

# smtp送信手順
server.ehlo() # ehloで接続
server.starttls() # tlsで接続
server.ehlo() # ehloで接続
server.login(username, password) # サーバへログイン
server.send_message(msg) # メールの送信
server.quit() # 接続の終了