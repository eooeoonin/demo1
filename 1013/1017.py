from appium import webdriver

caps = {}
caps["appActivity"] = "com.dkkj.modules.SplashPage"
caps["appPackage"] = "com.citiccard.mobilebank"
caps["platformName"] = "Android"
caps["deviceName"] = "111"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)