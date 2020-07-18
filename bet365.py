from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

driver.set_window_position(0, 0)
driver.set_window_size(375, 812)
driver.get('https://mobile.bet365.it/#/AC/B1/C1/D13/E49487629/F2/')

try:
    element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "gl-MarketGroup_Wrapper")))
    page = driver.page_source
finally:
    driver.quit()

print(page)
