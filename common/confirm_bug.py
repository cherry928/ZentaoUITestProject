import time
from selenium.webdriver.common.by import By

def confirm_bug(driver, title):
    driver.find_element(By.XPATH, '//a[contains(@href, "m=qa&f=index")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "m=bug&f=browse")]').click()
    driver.find_element(By.XPATH, '//a[contains(@href, "&branch=0&browseType=unclosed")]').click()
    driver.find_element(By.XPATH, '//a[text()="%s"]' % title).click()
    driver.find_element(By.XPATH, '//a[contains(@href, "m=bug&f=confirmBug")]').click()
    driver.switch_to.frame("iframe-triggerModal")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="D:开发人员1"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(5)
    driver.switch_to.default_content()