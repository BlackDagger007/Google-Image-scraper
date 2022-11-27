import webbrowser
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import urllib.request
import time
import os

CHROME_DRIVER_PATH = r"driver/chromedriver.exe"
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

keyword = input('Enter Search Term: ')
img_count = int(input('Enter Number of Images: '))

SEARCH_URL = f"https://www.google.com/search?q={keyword.replace(' ', '+')}&source=lnms&tbm=isch"

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=op)


# functions
def click_element_css(css):
    start = time.time()
    element_found = False
    while not element_found:
        try:
            e = driver.find_element(By.CSS_SELECTOR, css).text
            element_found = True
            driver.find_element(By.CSS_SELECTOR, css).click()
            return True
        except NoSuchElementException:
            end = time.time()
            if end - start >= 3:
                return False
            pass


def found_element_css(css):
    start = time.time()
    while True:
        try:
            e = driver.find_element(By.CSS_SELECTOR, css).text
            return True
        except NoSuchElementException:
            end = time.time()
            if end-start >= 10:
                return False
            pass


driver.get(SEARCH_URL)

# find imageTiles
downloads_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads').replace("\\", "/")
new_folder_path = f"{downloads_path}/_{keyword.replace(' ', '_')}"
os.makedirs(new_folder_path)

count = 0
img_tiles_css = '.wXeWr.islib.nfEiy'
for img_tile in driver.find_elements(By.CSS_SELECTOR, img_tiles_css):
    if not count < img_count:
        break
    img_tile.click()
    if found_element_css('.n3VNCb.KAlRDb'):
        count += 1
        img_src = driver.find_element(By.CSS_SELECTOR, '.n3VNCb.KAlRDb').get_attribute('src')
        urllib.request.urlretrieve(img_src, f"{new_folder_path}/{count}.jpg")

webbrowser.open(new_folder_path.replace('/', '//'))
print('Done!!!')
