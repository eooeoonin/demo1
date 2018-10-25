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
driver.implicitly_wait(5)

driver.find_element_by_id("com.xueqiu.android:id/agree").click()
driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon").click()
driver.find_element_by_id("com.xueqiu.android:id/tv_login").click()
driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others").click()
driver.find_element_by_id("com.xueqiu.android:id/register_phone_number").send_keys("18611920559")
#driver.get_screenshot_as_file("login.png")
#print(driver.page_source)
#el6 = driver.find_element_by_id("com.xueqiu.android:id/register_code_text")
#el6.click()
#driver.implicitly_wait(5)

driver.find_element_by_id("com.xueqiu.android:id/register_code").send_keys("111111")

driver.find_element_by_id("com.xueqiu.android:id/button_next").click()

# driver.quit()