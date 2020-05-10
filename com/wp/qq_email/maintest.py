#coding=utf-8

from com.wp.qq_email.decorator import *
import time

def login():
    ##  登录框iframe
    iframe = driver.find_element_by_id("login_frame")
    driver.switch_to.frame(iframe)
    driver.find_element_by_id("u").send_keys(readConfig("username"))
    driver.find_element_by_id("p").send_keys(readConfig("password"))
    driver.find_element_by_id("login_button").click()
    driver.switch_to.default_content()  ##  登录框iframe结束
    time.sleep(5)

def edit_email(msg):
    driver.find_element_by_xpath("/html/body[@class='frame_class']/div[@id='resize']/div[@id='leftPanel']/div[@id='navBarDiv']/ul[@id='navBarTd']/li[@id='composebtn_td']/a[@id='composebtn']").click()
    time.sleep(3)
    ##  收件人/主题/正文框iframe
    iframe = driver.find_element_by_xpath("/html/body/div[3]/div[6][@id='mainFrameContainer']/iframe[@id='mainFrame']")
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath("/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input").send_keys(readConfig("sender"))
    driver.find_element_by_id("subject").send_keys(unicode("测试", 'utf-8'))
    ##  正文框单独iframe
    iframe = driver.find_element_by_class_name("qmEditorIfrmEditArea")
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath('/html/body/div').send_keys(unicode(msg, 'utf-8'))
    driver.switch_to.parent_frame()  ##  正文框单独iframe结束

def send():
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/form[2]/div[3]/div/a[1]").click()
    driver.switch_to.default_content()  ##  收件人/主题/正文框iframe结束
    time.sleep(3)

def logout():
    driver.find_element_by_class_name("toptitle").click()
    time.sleep(3)
    driver.quit()

def main():
    login() ## 登录
    edit_email(readConfig("msg")) ## 编辑
    send() ## 发送
    logout() ## 退出

if __name__ == "__main__":
    main()