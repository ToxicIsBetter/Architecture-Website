import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1280, 800)

driver.get('http://localhost:3000')
time.sleep(2)
driver.save_screenshot('screenshot1.png')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight/2);')
time.sleep(2)
driver.save_screenshot('screenshot2.png')

driver.quit()
