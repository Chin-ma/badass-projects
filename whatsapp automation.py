from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as auto
import time
auto.PAUSE = 1

class whats_automater:

    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://web.whatsapp.com')
    a = input()

    def send_someone(self, person):
        search_butt = whats_automater.browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_butt.click()
        search_butt.send_keys(person)
        search_butt.send_keys(Keys.ENTER)
    def send_message(self, message):
        search_box = whats_automater.browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        search_box.click()
        search_box.send_keys(message)
        search_box.send_keys(Keys.ENTER)
    def send_files(self, file_link):
        time.sleep(4)
        attach_butt = whats_automater.browser.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        attach_butt.click()
        time.sleep(3)
        x, y, l, b = auto.locateOnScreen('document_button.PNG')
        a,b = auto.center((x,y,l,b))
        auto.click(a,b)
        time.sleep(4)
        auto.typewrite(file_link)
        auto.press('enter')
        time.sleep(5)
        enter_button = whats_automater.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')
        enter_button.click()

automate_now = whats_automater()
automate_now.send_someone('chiniboy')
automate_now.send_message('u r the biggest chutiya in the world')
automate_now.send_files("C:\\Users\\Pranil.DESKTOP-TLQKP4G.000\\Desktop\\selena.jpg")
#browser.quit()
