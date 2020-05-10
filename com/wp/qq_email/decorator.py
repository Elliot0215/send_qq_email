#coding=utf-8

from selenium import webdriver
from com.wp.qq_email.readconfig import *
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(readConfig("url"))

def login_dec(func):
    def wrapper(*args,**kwargs):
        ##  登录框iframe
        iframe = driver.find_element_by_id("login_frame")
        driver.switch_to.frame(iframe)
        driver.find_element_by_id("u").send_keys(readConfig("username"))
        driver.find_element_by_id("p").send_keys(readConfig("password"))
        driver.find_element_by_id("login_button").click()
        driver.switch_to.default_content()  ##  登录框iframe结束
        time.sleep(5)
        func(*args,**kwargs)
    return wrapper