from appium.webdriver.common.touch_action import TouchAction


class Swipe(self, driver):
    size=driver.get_window_size()
    width=size("width")
    height=size("height")

    print("device width is:",width)
    print("device height is:",height)

    def swipe_up(self):
        x=self.width*0.2
        y1=self.height*0.8
        y2=self.heigth*0.2
        TouchAction(driver).press(x,y1).move_to(x,y2).release().perform()

    def swipe_down(self):
        x = self.width * 0.2
        y1 = self.height * 0.2
        y2 = self.heigth * 0.8
        TouchAction(driver).press(x, y1).move_to(x, y2).release().perform()

    def swipe_left(self):
        x1=self.width*0.8
        x2=self.height*0.2
        y=self.heigth*0.2
        TouchAction(driver).press(x1,y).move_to(x2,y).release().perform()

    def swipe_right(self):
        x1=self.width*0.2
        x2=self.height*0.8
        y=self.heigth*0.2
        TouchAction(driver).press(x1,y).move_to(x2,y).release().perform()