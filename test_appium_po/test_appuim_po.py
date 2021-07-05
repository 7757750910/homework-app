import logging
import allure
from faker import Faker

from test_appium.test_appium_po.pages.mainpage import PageMain


@allure.feature("企业微信app通讯录")
class TestContact():
    def setup_class(self):
        self.fake = Faker('zh_CN')

    def setup(self):
        logging.info("--- 实例化主页对象 ---")
        self.page_main = PageMain()

    def teardown(self):
        self.page_main.close_driver()

    @allure.story("添加成员")
    @allure.title("添加成员")
    def test_add_member(self):
        name = self.fake.name()
        phone = self.fake.phone_number()
        result = self.page_main.click_contact().click_add_member().choose_by_manual().edit_member(name, phone)
        assert '保存成功' == result
