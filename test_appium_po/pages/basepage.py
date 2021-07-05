import logging

import Faker as Faker
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class Base:

    def __init__(self, driver_base: WebDriver = None):
        if not driver_base:
            caps = dict()
            caps['platformName'] = "android"
            caps['appPackage'] = "com.tencent.wework"
            caps['appActivity'] = ".launch.LaunchSplashActivity"
            caps['noReset'] = "true"
            caps['deviceName'] = "Clifford"
            caps['skipDeviceInitialization'] = 'true'
            caps['settings[waitForIdleTimeout'] = 0
            caps['dontStopAppOnReset'] = True
            logging.info("实例化driver对象")
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver_base

    # 查找
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 滑动
    def find_with_scroll(self, text: str):
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                           f'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("{text}").instance(0));')
        self.driver.implicitly_wait(5)
        return element

    # 查找点击
    def find_and_click(self, by, locator):
        element = self.driver.find_element(by, locator).click()
        return element

    # 关闭
    def close_driver(self):
        logging.info("关闭driver")
        self.driver.close()
