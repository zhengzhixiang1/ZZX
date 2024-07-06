# 淘宝秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time
from os import path
from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

driver = webdriver.Firefox()
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录.
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()

    print("请在30秒内完成扫码")
    time.sleep(30)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    # # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_CheckBox_939775250537"):
    #  driver.find_element_by_id("J_CheckBox_939775250537").click()
    # if driver.find_element_by_id("J_CheckBox_939558169627"):
    #  driver.find_element_by_id("J_CheckBox_939558169627").click()
    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S:%f'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("当前时间" + now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text('提交订单').click()
            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2021M S-12-26 23:20:00.000000"
    login()
    buy("2021-12-28 15:59:00.000000")
