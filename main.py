from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


drive = webdriver.Chrome()

drive.get(
    "https://app.ringba.com/#/login"
)
wait = WebDriverWait(drive, 25)
drive.maximize_window()
action = ActionChains(drive)
username = wait.until(EC.element_to_be_clickable((By.ID, "userName")))
# drive.find_element(By.ID, "userName")
username.click()

username.send_keys("info@ray-advertising.com")

password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
password.click()
password.send_keys("Ray@2021")

submit = wait.until(EC.element_to_be_clickable((By.ID, "login-form-submit")))
submit.click()

report = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "a[ng-click='vm.reportsExpanded = !vm.reportsExpanded']"))).click()

default = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "span[title='Create a new custom Call Logs Report']"
))).click()

dateSelector = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "div[class='daterangepicker-btn m-b-10 reporting-settings-v2__date-picker btn m-l-10'] span"
))).click()

date = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "li[data-range-key='Last 2 days']"
))).click()


elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main-content"]/div[3]/div/div/call-log-vue-container/div/div[2]/div[5]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div')))

numbers = []
for e in elements:
    callIds = wait.until(EC.presence_of_all_elements_located((
       By.XPATH,
       "//div[@col-id='inboundPhoneNumber']"
        )))
    # print([d])
    for c in callIds:
        numbers.append(c.text)


time.sleep(0.5)
my_dict = {
    "numbers": numbers
}
now = datetime.now()
month_day_year = now.strftime("%m%d%y")
print(my_dict)
df = pd.DataFrame(my_dict)
df.to_json(f"{month_day_year}.json", orient='records', lines=True)
drive.close()
