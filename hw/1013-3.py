# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["appActivity"] = "com.xueqiu.android.common.SplashActivity"
caps["appPackage"] = "com.xueqiu.android"
caps["platformName"] = "Android"
caps["deviceName"] = "111"
caps["unicodeKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

driver.find_element_by_id("com.xueqiu.android:id/cancel").click()
time.sleep(5)
driver.find_element_by_xpath("(//android.widget.ImageView[@resource-id='com.xueqiu.android:id/tab_icon'])[4]").click()
#driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.xueqiu.android:id/tab_icon' and @instance=17]").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='板块' and @resource-id='com.xueqiu.android:id/text']").click()
driver.find_element_by_xpath("//android.widget.ImageView[@instance=1]").click()
TouchAction(driver).press(x=300, y=2400).move_to(x=300, y=300).release().perform()
time.sleep(5)
TouchAction(driver).press(x=300, y=2400).move_to(x=300, y=300).release().perform()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='食品饮料']").click()
TouchAction(driver).press(x=300, y=2400).move_to(x=300, y=300).release().perform()
time.sleep(5)
TouchAction(driver).press(x=300, y=2400).move_to(x=300, y=300).release().perform()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.ListView[@resource-id='com.xueqiu.android:id/listview']/android.widget.LinearLayout[last()]/android.widget.LinearLayout/android.widget.TextView[1]").click()