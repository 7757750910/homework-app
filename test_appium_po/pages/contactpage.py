import logging
import time

import allure
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.pages.basepage import Base


# 通讯录页
class PageContact(Base):
    _ADD_MEMBER = (MobileBy.XPATH, "//*[@text='添加成员']")
    with allure.step('点击添加成员'):
        def click_add_member(self):
            logging.info('滑动查找添加成员按钮')
            self.find_with_scroll('添加成员')
            logging.info("点击添加成员")
            self.find_and_click(*self._ADD_MEMBER)
            from test_appium.test_appium_po.pages.addcontantpage import PageContactAddChoose
            return PageContactAddChoose(self.driver)
