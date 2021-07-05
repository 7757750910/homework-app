import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.pages.basepage import Base


# 主页
class PageMain(Base):
    _MENU_CONTACT = (MobileBy.XPATH, "//*[@text='通讯录']")
    with allure.step('点击通讯录，进入通讯录界面'):
        def click_contact(self):
            logging.info("点击通讯录")
            self.find_and_click(*self._MENU_CONTACT)
            from test_appium.test_appium_po.pages.contactpage import PageContact
            return PageContact(self.driver)
