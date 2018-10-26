import unittest
from appium import webdriver

class ATests(unittest.TestCase):
    def setUp(self):
        caps = {}
        caps["appActivity"] = "com.xueqiu.android.common.SplashActivity"
        caps["appPackage"] = "com.xueqiu.android"
        caps["platformName"] = "Android"
        caps["deviceName"] = "111"
        caps["unicodeKeyboard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_PageSource(self):
        #print("111",self.driver.page_source)
        for x in self.driver.find_elements_by_xpath("//*"):
            print("text=",x.text)
            print("location",x.location)
