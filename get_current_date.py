from selenium.webdriver.common.by import By
from datetime import datetime

driver.get('file:///app/group.html')
date_str = ' '.join(driver.find_elements(by=By.CLASS_NAME, value="consular-appt")[0].text.split(' ')[2:5])
datetime.strptime(date_str, '%d %B, %Y,')
