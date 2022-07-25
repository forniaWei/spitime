from selenium import webdriver
from selenium.webdriver.common.by import By
from common.screen import getScreen
from common.send_email import email
import time
from datetime import datetime
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(1)
time_now = str(datetime.now())

def data():
    driver.get('https://dev.qilinhuicloud.com/?#/login')
    driver.find_element(By.ID, 'coordinated_name').send_keys('jjadminT')
    driver.find_element(By.ID, "coordinated_password").send_keys("Abc123!")
    driver.find_element(By.CLASS_NAME, "ant-btn-round").click()
    print(driver.page_source)
    print(driver.current_url)
    print(driver.title)
    if  driver.current_url != 'https://dev.qilinhuicloud.com/?#/homeIndex':
        now = time_now.strftime("%Y-%m-%d %H:%M")
        getScreen(driver,now)

        email('D:\定时任务\pictures'+now+ ".png")

