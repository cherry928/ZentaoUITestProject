import time
from selenium.webdriver.common.by import By

def create_bug(driver, title):
    driver.find_element(By.XPATH, '//a[substring(@href,23)="m=qa&f=index"]').click()
    driver.find_element(By.XPATH, '//a[contains(@href,"m=bug&f=browse&productID=1")]').click()
    driver.find_element(By.XPATH,
                        '//a[@href="/zentao/www/index.php?m=bug&f=create&productID=1&branch=0&extra=moduleID=0"]').click()

    driver.find_element(By.XPATH, '//div[@id="product_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="学生成绩管理系统"]').click()

    driver.find_element(By.XPATH, '//div[@id="module_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="/年级成绩管理"]').click()

    driver.find_element(By.XPATH, '//div[@id="project_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="湖南中医药测试实训"]').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="v2.0"]').click()

    driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="D:开发人员2"]').click()

    driver.find_element(By.XPATH, '//input[@id="deadline"]').send_keys('2020-04-08')

    driver.find_element(By.XPATH, '//div[@id="type_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="性能问题"]').click()

    driver.find_element(By.XPATH, '//div[@id="os_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="Windows 7"]').click()

    driver.find_element(By.XPATH, '//div[@id="browser_chosen"]').click()
    driver.find_element(By.XPATH, '//li[@title="IE11"]').click()

    driver.find_element(By.XPATH, '//input[@id="title"]').send_keys(title)

    driver.find_element(By.XPATH, '//div[@data-type="severity"]').click()
    driver.find_element(By.XPATH, '//span[@data-value="2"]').click()

    driver.find_element(By.XPATH, '//div[@data-type="pri"]').click()
    driver.find_element(By.XPATH, '//span[@data-value="2" and contains(@class, "label-pri")]').click()

    content_frame = driver.find_element(By.XPATH, '//iframe[@class="ke-edit-iframe"]')
    driver.switch_to.frame(content_frame)
    driver.find_element(By.XPATH, '//body').clear()
    driver.find_element(By.XPATH, '//body').send_keys(
        '<p>[步骤]</p>1、点击首页；2、查看页面显示<br><p>[结果]</p>1、页面显示正常<br><p>[期望]</p>1、页面线条太粗<br>')
    driver.switch_to.default_content()

    # 滚动到指定元素
    element = driver.find_element(By.XPATH, '//div[@id="mailto_chosen"]')
    driver.execute_script('arguments[0].scrollIntoView();', element)
    time.sleep(2)
    element.click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@id="mailto_chosen"]/div/ul/li[@title="T:测试人员2"]').click()

    driver.find_element(By.XPATH, '//button[@id="submit"]').click()