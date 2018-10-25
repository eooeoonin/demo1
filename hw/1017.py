from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["appActivity"] = "com.dkkj.modules.SplashPage"
caps["appPackage"] = "com.citiccard.mobilebank"
caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:62001"
caps["noReset"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)

driver.find_element_by_xpath("//android.widget.TextView[@text='积分']").click()
driver.find_element_by_xpath("//android.widget.ImageView[@instance=8]").click()
TouchAction(driver).press(x=300, y=2400).move_to(x=300, y=300).release().perform()
driver.find_element_by_xpath("(//android.view.View[@content-desc='Link'])[2]").click()

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
driver.swipe()

