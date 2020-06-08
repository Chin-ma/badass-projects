from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as auto
import time
from all_cred import spotify_cred


class spotify_automater:
    web = webdriver.Chrome('chromedriver.exe')
    web.get('https://open.spotify.com/?_ga=2.75499349.1760950225.1591637652-464591607.1590344537')

    def login(self):
        log_butt = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[4]/button[2]')
        log_butt.click()
        time.sleep(8)
        email_butt = spotify_automater.web.find_element_by_xpath('//*[@id="login-username"]')
        email_butt.click()
        email_butt.send_keys(spotify_cred['username'])
        password_butt = spotify_automater.web.find_element_by_xpath('//*[@id="login-password"]')
        password_butt.click()
        password_butt.send_keys(spotify_cred['password'])
        final_log = spotify_automater.web.find_element_by_xpath('//*[@id="login-button"]')
        final_log.click()
        time.sleep(8)
    def play_my_playlist(self):
        my_lib = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[3]/div/a')
        my_lib.click()
        time.sleep(4)
        playlist_butt = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[1]/div/div')
        playlist_butt.click()
        time.sleep(4)
        play_butt = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button')
        play_butt.click()
    def play_music(self, music):
        search_butt = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/nav/ul/li[2]/a')
        search_butt.click()
        time.sleep(2)
        auto.typewrite(music)
        time.sleep(4)
        song_butt = spotify_automater.web.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div/div[2]')
        song_butt.click()
        time.sleep(2)
        play_butt = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button[1]')
        play_butt.click()
    def resume_pause_music(self):
        res_butt = spotify_automater.web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[3]/footer/div/div[2]/div/div[1]/div[3]')
        res_butt.click()

spotify = spotify_automater()
spotify.login()
spotify.play_music('sage')



