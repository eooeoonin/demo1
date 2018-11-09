from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from appium import webdriver


page = (MobileBy.ID, "com.jjy.p2p:id/iv_sp_start")


def get_lastpage():
    lastpage = (By.ID, "com.jjy.p2p:id/btn_splash3_start")
    return lastpage