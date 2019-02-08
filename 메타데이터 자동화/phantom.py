from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/jinyoung/Desktop/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(5)

base_url = 'http://factcheck.snu.ac.kr/v2/facts/27'
driver.get(base_url)

try:
    driver.find_element_by_xpath('//*[@class="reg_date"]/p/a').click()

    modi_result = driver.find_element_by_xpath('//*[@class="meter-label"]').text
    print(modi_result)

    driver.find_elements_by_xpath('//*[@class="reg_date"]/ul/li')[-1].click()
    time.sleep(5)
    org_result = driver.find_element_by_xpath('//*[@class="meter-label"]').text
    print(org_result)

except:
    modi_result = driver.find_element_by_xpath('//*[@class="meter-label"]').text
    print(modi_result)