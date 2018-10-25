# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["appActivity"] = "com.xueqiu.android.common.SplashActivity"
caps["appPackage"] = "com.xueqiu.android"
caps["platformName"] = "Android"
caps["deviceName"] = "111"
caps["unicodeKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

driver.find_element_by_id("com.xueqiu.android:id/cancel").click()
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("小米")
driver.find_element_by_xpath("//*[@text='小米集团-W'and @resource-id='com.xueqiu.android:id/stockName']").click()

#driver.quit()
