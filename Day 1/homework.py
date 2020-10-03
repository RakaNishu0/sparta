from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('../venv/chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EA%B3%B5%EC%9C%A0")
time.sleep(3)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select("#imgList > div > a > img")

i = 1
for thumbnail in thumbnails:
    thumb = thumbnail['src']
    dload.save(thumb, f'img_share/{i}.jpg')
    i += 1

driver.quit()       # 끝나면 닫아주기
