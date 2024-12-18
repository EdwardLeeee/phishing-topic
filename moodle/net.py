from selenium import webdriver
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import requests

# 設定 Chrome 瀏覽器
driver = webdriver.Chrome()

# 打開目標頁面
url = 'https://moodle3.ntnu.edu.tw/login/index.php'
driver.get(url)

# 等待頁面內容渲染完成
time.sleep(5)

# 獲取渲染後的 HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 保存渲染後的 HTML 到本地
with open("index.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# 抓取所有圖片並下載
for img in soup.find_all('img'):
    img_url = img.get('src')
    if img_url:
        full_img_url = urljoin(url, img_url)
        print(f"Downloading: {full_img_url}")
        img_response = requests.get(full_img_url)
        img_name = full_img_url.split("/")[-1]
        with open(img_name, "wb") as img_file:
            img_file.write(img_response.content)

# 關閉瀏覽器
driver.quit()

