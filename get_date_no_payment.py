from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('file:///app/payment_page_2.html')
res = {}
for i in range(1, 3):
    location = driver.find_elements(by=By.XPATH, value=f'//*[@id="paymentOptions"]/div[2]/table/tbody/tr[{i}]/td[1]')[0].text
    status = driver.find_elements(by=By.XPATH, value=f'//*[@id="paymentOptions"]/div[2]/table/tbody/tr[{i}]/td[2]')[0].text
    res[location] = status
print(res)
