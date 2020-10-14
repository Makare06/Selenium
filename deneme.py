from selenium import webdriver
import time
from deneme2 import User

usr = User()
ka = usr.getkullaniciad()
ks = usr.getsifre()
class signIn:

    def __init__(self,ka,ks):
        self.kullanici_ad = ka
        self.sifre = ks
        self.browser_options = webdriver.ChromeOptions()
        self.browser_options.add_experimental_option("excludeSwitches",['enable-automation'])
        self.browser = webdriver.Chrome(options=self.browser_options)
        
    def login(self):

        time.sleep(3)
        self.browser.maximize_window()
        self.browser.get("http://173.212.227.23/")
        time.sleep(3)
        self.browser.find_element_by_id("username").send_keys(self.kullanici_ad)
        self.browser.find_element_by_id("current-password").send_keys(self.sifre)
        time.sleep(1)
        self.browser.find_element_by_id("login-btn").click()
        time.sleep(5)
cs = signIn(ka,ks)
cs.login()