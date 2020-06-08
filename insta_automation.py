from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests, webbrowser
import pyautogui as auto
import time, os
from PIL import Image
from insta_cred import cred

class insta_automater:
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get('https://www.instagram.com')
    time.sleep(3)

    def login(self, username, password):
        user_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        user_butt.click()
        user_butt.send_keys(username)
        pass_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        pass_butt.click()
        pass_butt.send_keys(password)
        log_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        log_butt.click()
        time.sleep(3)
        save_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button')
        save_butt.click()
        time.sleep(2)
        notif_butt = insta_automater.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notif_butt.click()

    def post_something(self, photo_location, caption):
        auto.hotkey('ctrl', 'shift', 'i')
        time.sleep(3)
        x, y, l, b = auto.locateOnScreen('toggle_device_toolbar.PNG')
        a,b = auto.center((x,y,l,b))
        auto.click(a,b)
        auto.press('f5')
        time.sleep(4)
        x, y, l, b = auto.locateOnScreen('cancel_wind.PNG')
        a,b = auto.center((x,y,l,b))
        auto.click(a,b)
        time.sleep(5)
        cancel_butt = insta_automater.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        cancel_butt.click()
        time.sleep(5)
        add_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        add_butt.click()
        time.sleep(2)
        auto.typewrite(photo_location)
        auto.press('enter')
        time.sleep(2)
        next_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]')
        next_butt.click()
        time.sleep(2)
        caption_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]')
        caption_butt.click()
        auto.typewrite(caption)
        time.sleep(1)
        share_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]')
        share_butt.click()
        insta_automater.browser.quit()
    def download_latest_post(self, name, img_save_location):
        time.sleep(2)
        search_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
        search_butt.click()
        search_bar = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(name)
        time.sleep(2)
        name_butt = insta_automater.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]')
        name_butt.click()
        time.sleep(4)
        for i in range(15):
            auto.keyDown('down')
        post = insta_automater.browser.find_element_by_class_name('KL4Bh')
        image = post.find_element_by_tag_name('img')
        image = image.get_attribute('src')
        auto.hotkey('ctrl', 't')
        time.sleep(2)
        auto.typewrite(image)
        auto.press('enter')
        time.sleep(2)
        auto.hotkey('ctrl', 's')
        time.sleep(3)
        image_name = f'{name}.jpg'
        auto.typewrite(image_name)
        x, y, l, b = auto.locateOnScreen('download_button.PNG')
        a,b = auto.center((x,y,l,b))
        auto.click(a,b)
        time.sleep(2)
        auto.typewrite(img_save_location)
        n = len(img_save_location.split('\\'))+2
        for i in range(n):
            auto.press('enter')
        insta_automater.browser.quit()
        time.sleep(3)
        img_path = f'{img_save_location}\\{image_name}'
        img = Image.open(img_path)
        img.show()
        a = input('press yes if you wanna delete the image\n')
        if a=='yes':
            os.remove(img_path)
        else:
            pass



ins_info = insta_automater()
ins_info.login(cred['username'], cred['password'])
ins_info.download_latest_post('tara', 'E:\\pranil\\python\\doing shit with python')


