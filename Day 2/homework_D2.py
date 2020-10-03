from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

driver = webdriver.Chrome('../chromedriver')

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%ED%8A%B8%EB%9F%BC%ED%94%84+%EC%BD%94%EB%A1%9C%EB%82%98&oquery=%EC%B6%94%EC%84%9D&tqi=U3luslp0YihssD%2FR6L0ssssstod-438521"

driver.get(url)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

article = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

for articles in article:
    title = articles.select_one('dl > dt > a').text
    article_url = articles.select_one('dl > dt > a')['href']
    journal = articles.select_one('dl > dd > span').text.split(' ')[0].replace('언론사', '')
    thumb = articles.select_one('div > a > img')['src']
    # print(title, article_url, journal, thumb)
    ws1.append([title, article_url, journal, thumb])

driver.quit()

wb.save(filename='articles.xlsx')


# 첨부해서 메일 보내기
# 보내는 사람 정보
me = "getouthere0@gmail.com"
my_password = ""

# 로그인 하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
# you = "getouthere0@naver.com"

# 반복문 넣어서 복수 계정에 메일 보내기
emails = ['getouthere0@naver.com', 'getouthere0@naver.com']

for you in emails:
    # 메일 정보 기본 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "스파르타 2일차 과제"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "기사 스크랩 / 트럼프 코로나 / 썸네일 포함 / 엑셀 저장 / 파일첨부 / 메일 송수신"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="도람푸_코로나.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())

s.quit()
