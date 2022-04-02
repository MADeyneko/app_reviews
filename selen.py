import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class FindByXpathCss():
        driver = webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
        driver.maximize_window()
        baseUrl = "https://play.google.com/store/apps/details?id=com.sberauto.mobile&hl=en_US&showAllReviews=true"
        driver.get(baseUrl)

        scrolls = 15
        while True:
            scrolls -= 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            if scrolls < 0:
                break

        elemtn = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'RveJvd snByac')]")))
        elemtn.click()

        scrolls = 5
        while True:
            scrolls -= 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            if scrolls < 0:
                break

        elemtn = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'RveJvd snByac')]")))
        elemtn.click()
        reviewText = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@class='UD7Dzf']")))

        # reviewText = driver.find_elements_by_xpath("//*[@class='UD7Dzf']")
        for textreview in reviewText:
            print(textreview.text)

if __name__=='__main__':
    FindByXpathCss()