import logging

import allure
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_appium_po.pages.basepage import Base


# 添加成员页
class PageContactAddChoose(Base):
    _ITEM_ADD_BY_MANUAL = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    with allure.step('点击手工输入添加'):
        def choose_by_manual(self):
            logging.info("点击手工输入添加")
            self.find_and_click(*self._ITEM_ADD_BY_MANUAL)
            from test_appium.test_appium_po.pages.editcontantpage import PageContactAddEdit
            return PageContactAddEdit(self.driver)
