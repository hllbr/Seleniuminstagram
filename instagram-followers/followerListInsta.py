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

procedur1 =browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
procedur1.click()
procedur2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
procedur2.click()
time.sleep(10)


#profil area
profıl_editon = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[1]")
profıl_editon.click()

time.sleep(5)
buttons = browser.find_elements_by_css_selector("._bnq48")

followersButton = buttons[1]

followersButton.click()


time.sleep(5)
browser.close()
