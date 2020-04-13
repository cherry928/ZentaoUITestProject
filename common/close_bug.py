import time
from selenium.webdriver.common.by import By

def close_bug(driver, title):
    driver.refresh()
    driver.find_element(By.XPATH, '//a[contains(@href, "m=qa&f=index")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "m=bug&f=browse")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "&branch=0&browseType=assigntome")]').click()
    driver.find_element(By.XPATH, '//a[text()="%s"]' % title).click()
    driver.find_element(By.XPATH, '//span[text()="关闭"]').click()
    driver.switch_to.frame('iframe-triggerModal')
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(1)
    driver.switch_to.default_content()
