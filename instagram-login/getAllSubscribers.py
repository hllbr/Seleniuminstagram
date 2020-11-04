from selenium import webdriver
import time
import loginInfo
browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")
time.sleep(2)

#login area

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

loginButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
loginButton.click()

time.sleep(10)

browser.close()
