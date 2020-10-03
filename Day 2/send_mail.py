import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
me = "getouthere0@gmail.com"
my_password = "Hwan6165!"

# 로그인 하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
# you = "getouthere0@naver.com"

# 반복문 넣어서 복수 계정에 메일 보내기
emails = ['getouthere0@daum.net', 'getouthere0@naver.com', 'getouthere0@naver.com']

for you in emails:
    # 메일 정보 기본 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "제목 없어 2"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "내용이 없습니다"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())

s.quit()
