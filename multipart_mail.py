from email.mime import multipart
from email.mime import text
import smtplib

import config

# 基本情報
smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = config.from_email
to_email = config.to_email
username = config.username
password = config.password

# メール
msg = multipart.MIMEMultipart() 
msg.attach(text.MIMEText("テストメールです。", "plain"))
msg['Subject'] = "テストメールの件名です。"
msg["From"] = from_email
msg["To"] = to_email
with open("multipart_mail.py", "r") as f:
    attachment = text.MIMEText(f.read(), "plain")
    attachment.add_header(
        "Content-Disposition", "attachment", filename="test.py"
    )
    msg.attach(attachment)


# サーバインスタンス作成
server = smtplib.SMTP(host=smtp_host, port=smtp_port)

# smtp送信手順
server.ehlo() # ehloで接続
server.starttls() # tlsで接続
server.ehlo() # ehloで接続
server.login(username, password) # サーバへログイン
server.send_message(msg) # メールの送信
server.quit() # 接続の終了