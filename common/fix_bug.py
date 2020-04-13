import time
from selenium.webdriver.common.by import By

def fix_bug(driver, title):
    driver.find_element(By.XPATH, '//a[contains(@href, "m=qa&f=index")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "m=bug&f=browse")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "&branch=0&browseType=assigntome")]').click()
    driver.find_element(By.XPATH, '//a[text()="%s"]' % title).click()
    driver.find_element(By.XPATH, '//a[contains(@href, "m=bug&f=resolve")]').click()
    driver.switch_to.frame('iframe-triggerModal')
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@id="resolution_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="已解决"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@id="resolvedBuild_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="v2.0"]').click()
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(5)
    driver.switch_to.default_content()