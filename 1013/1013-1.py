# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["appActivity"] = "com.xueqiu.android.common.SplashActivity"
caps["appPackage"] = "com.xueqiu.android"
caps["platformName"] = "Android"
caps["deviceName"] = "111"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.

el1 = driver.find_element_by_id("com.xueqiu.android:id/agree")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/register_phone_number")
el5.send_keys("18611920559")
el6 = driver.find_element_by_id("com.xueqiu.android:id/register_code_text")
el6.click()

el7 =river.find_element_by_id("com.xueqiu.android:id/register_code")
el7.send_keys("111111")
el8 = driver.find_element_by_id("com.xueqiu.android:id/button_next")
el8.click()




# driver.quit()