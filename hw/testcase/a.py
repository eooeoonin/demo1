import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from hw.po import main, login
from hw.po.welcome import get_lastpage, page


class ATests(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["appActivity"] = "com.jjy.p2p.activity.OpenActivity"
        caps["appPackage"] = "com.jjy.p2p"
        caps["platformName"] = "Android"
        caps["deviceName"] = "111"
        caps["unicodeKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
       # sleep(10)

        for i in range(3):
            if (self.driver.find_element(*page)):
                TouchAction(self.driver).press(x=1200, y=1000).move_to(x=300, y=1000).release().perform()

        self.driver.find_element(*get_lastpage()).click()
        sleep(5)
        #self.driver.find_element_by_id("com.jjy.p2p:id/btn_splash3_start").click()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element(*main.button_zh).click()
        self.driver.find_element(*login.username).send_keys("18611920559")
        self.driver.find_element(*login.password).send_keys("333333")
        self.driver.find_element(*login.sure).click()

