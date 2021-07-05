import logging
import time

import allure
from appium.webdriver.common.mobileby import MobileBy
from faker import Faker

from test_appium.test_appium_po.pages.basepage import Base


# 编辑成员信息页
class PageContactAddEdit(Base):
    _MEMBER_NAME = (MobileBy.ID, "com.tencent.wework:id/b09")
    _MOBILE_NUM = (MobileBy.ID, "com.tencent.wework:id/f7y")
    _SAVE = (MobileBy.ID, "com.tencent.wework:id/ad2")
    _TOAST = (MobileBy.XPATH, '//*[contains(@text,"添加成功")]')
    with allure.step('输入成员信息'):
        def edit_member(self, name, phone):
            logging.info("录入成员信息")
            self.find(*self._MEMBER_NAME).send_keys(name)
            self.find(*self._MOBILE_NUM).send_keys(phone)
            logging.info("点击保存按钮")
            self.find_and_click(*self._SAVE)
            logging.info("提取toast提示信息")
            text = self.find(*self._TOAST).text
            time.sleep(2)
            return text
